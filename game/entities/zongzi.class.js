import Object from "../object.class.js";
import Game from "../game.class.js";

/**
 * 粽子收集物，取代原 Coin
 * type: 'north' | 'south' | 'alkaline'
 *
 * 北部粽 (north)  — +1分，蒸煮清爽
 * 南部粽 (south)  — +2分，炭火紮實，收集時回血 +5 HP
 * 鹼粽   (alkaline) — +3分，攜帶沾醬時觸發加成
 */
export default class Zongzi extends Object {

    name = 'zongzi';
    height = 90;
    width = 90;
    isCollected = false;
    hasHitbox = true;

    static SCORES = { north: 1, south: 2, alkaline: 3 };

    constructor(x, y, type = 'north') {
        super();

        this.game = new Game();
        this.x = x;
        this.y = y;
        this.type = type;

        this.animation = {
            frames: type === 'alkaline' ? 8 : 4,
            path: `./assets/items/${type}-zongzi/`,
            loop: true,
        };

        this.loadImage(`./assets/items/${type}-zongzi/0.png`);
        this.loadAnimation(this.animation);
        this.playAnimation(this.animation);
    }

    collect() {
        if (this.isCollected) return;
        this.isCollected = true;

        const score = Zongzi.SCORES[this.type] ?? 1;
        this.game.ui.addZongzi(score);

        this._applyEffect();
        this.remove();
        this.game.sounds.playSound('./assets/sounds/coin-collected.mp3', false, 0.3);
    }

    _applyEffect() {
        const character = this.game.world.level.character;

        if (this.type === 'south') {
            // 南部粽：回血 +5
            const healed = Math.min(5, 100 - character.health);
            if (healed > 0) {
                character.health += healed;
                this.game.ui.updateHealthbar();
            }
        }

        if (this.type === 'alkaline' && character.condimentCharge) {
            this._triggerCondimentBonus(character);
        }
    }

    _triggerCondimentBonus(character) {
        const type = character.condimentCharge;
        character.condimentCharge = null;
        this.game.ui.clearCondimentCharge();

        if (type === 'sugar') {
            // 砂糖 + 鹼粽 → 回血 +20
            const healed = Math.min(20, 100 - character.health);
            character.health += healed;
            this.game.ui.updateHealthbar();
            this.game.ui.showBonus('甜蜜加持！回血 +20');

        } else if (type === 'soysauce') {
            // 醬油 + 鹼粽 → 速度加成 5 秒
            character.speed *= 1.8;
            this.game.ui.showBonus('鮮鹹爆發！速度 x1.8（5秒）');
            setTimeout(() => {
                character.speed /= 1.8;
                this.game.ui.showBonus('速度恢復正常');
            }, 5000);
        }
    }

    remove() {
        const arr = this.game.world.level.coins;
        const idx = arr.indexOf(this);
        if (idx !== -1) arr.splice(idx, 1);
    }
}
