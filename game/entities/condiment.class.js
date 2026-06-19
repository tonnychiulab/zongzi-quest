import Object from "../object.class.js";
import Game from "../game.class.js";

/**
 * 沾醬道具，取代原 Poison
 * type: 'sugar' | 'soysauce'
 *
 * 撿到後給角色 condimentCharge（10秒有效期）
 * 在有效期間撿到鹼粽 → 觸發特殊效果
 */
export default class Condiment extends Object {

    name = 'condiment';
    isCollected = false;
    hasHitbox = true;
    hitboxRight = 0;
    hitboxLeft = 0;
    hitboxTop = 0;
    hitboxBottom = 0;

    CHARGE_DURATION = 10000; // 10 秒

    constructor(x, y, type = 'sugar') {
        super();

        this.game = new Game();
        this.x = x;
        this.y = y;
        this.type = type;

        const isBottle = type === 'soysauce';
        this.height = isBottle ? 164 : 120;
        this.width = isBottle ? 120 : 120;

        this.animation = {
            frames: 8,
            path: `../assets/items/${type}-animated/`,
            loop: true,
        };

        this.loadImage(`../assets/items/${type}-animated/0.png`);
        this.loadAnimation(this.animation);
        this.playAnimation(this.animation);
    }

    collect() {
        if (this.isCollected) return;
        this.isCollected = true;

        this.game.ui.addCondiment(this.type);
        this.remove();
        this._giveCharge();
        this._playSound();
    }

    _giveCharge() {
        const character = this.game.world.level.character;
        character.condimentCharge = this.type;
        character.condimentChargeTimer = setTimeout(() => {
            if (character.condimentCharge === this.type) {
                character.condimentCharge = null;
                this.game.ui.clearCondimentCharge();
            }
        }, this.CHARGE_DURATION);
    }

    _playSound() {
        const allCollected = this.game.ui.collectedCondiments === this.game.ui.totalCondiments;
        if (allCollected) {
            this.game.sounds.playSound('../assets/sounds/all-poison-collected.mp3', false, 0.4);
        } else {
            this.game.sounds.playSound('../assets/sounds/poison-collected.wav');
        }
    }

    remove() {
        const arr = this.game.world.level.poison;
        const idx = arr.indexOf(this);
        if (idx !== -1) arr.splice(idx, 1);
    }
}
