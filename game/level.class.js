import Character from "./entities/character.class.js";
import Jellyfish from "./entities/jellyfish.class.js";
import Pufferfish from "./entities/pufferfish.class.js";
import Zongzi from "./entities/zongzi.class.js";
import Condiment from "./entities/condiment.class.js";
import Barrier from "./entities/barrier.class.js";
import Boss from "./entities/boss.class.js";

/**
 * Level design
 * put following here:
 * - character
 * - boss
 * - enemies
 * - coins
 * - poision
 * - barriers
 * - background objects
 */

export default class Level {
  /**
   * Character
   */
  character = new Character();

  /**
   * Boss
   */
  boss = new Boss();

  /**
   * Enemies
   */
  enemies = [
    new Pufferfish(1930, 550),
    new Pufferfish(3700, 140),
    new Pufferfish(3680, 340),
    new Jellyfish(2300, "regular"),
    new Jellyfish(4500, "regular"),
    new Jellyfish(4700, "regular"),
    new Jellyfish(4900, "regular"),
    new Jellyfish(5100, "regular"),
    new Pufferfish(6400, 400),
    new Jellyfish(6850, "electric"),
  ];

  /**
   * 粽子（取代金幣）
   * 8 北部粽 / 8 南部粽 / 4 鹼粽 = 20 顆
   */
  coins = [
    // 北部粽（綠色，蒸煮）
    new Zongzi(1200, 400, 'north'),
    new Zongzi(1400, 400, 'north'),
    new Zongzi(1800, 400, 'north'),
    new Zongzi(2000, 400, 'north'),
    new Zongzi(3150, 330, 'north'),
    new Zongzi(3300, 330, 'north'),
    new Zongzi(3450, 330, 'north'),
    new Zongzi(3150, 190, 'north'),
    // 南部粽（深棕，炭火，回血）
    new Zongzi(3450, 190, 'south'),
    new Zongzi(4540, 500, 'south'),
    new Zongzi(4740, 500, 'south'),
    new Zongzi(4940, 500, 'south'),
    new Zongzi(5140, 500, 'south'),
    new Zongzi(7050, 300, 'south'),
    new Zongzi(7050, 500, 'south'),
    new Zongzi(7050, 700, 'south'),
    new Zongzi(7900, 450, 'south'),
    // 鹼粽（黃金，觸發沾醬加成）
    new Zongzi(7700, 450, 'alkaline'),
    new Zongzi(8100, 450, 'alkaline'),
    new Zongzi(8300, 450, 'alkaline'),
  ];

  /**
   * 沾醬道具（取代毒藥瓶）
   * 2 砂糖 + 3 醬油 = 5 個
   */
  poison = [
    new Condiment(1585, 330, 'sugar'),
    new Condiment(2300, 50,  'soysauce'),
    new Condiment(3285, 145, 'sugar'),
    new Condiment(4825, 780, 'soysauce'),
    new Condiment(7035, 50,  'soysauce'),
  ];

  /**Barriers */
  barriers = [
    new Barrier(750, 400, 0),
    new Barrier(950, -100, 1),
    new Barrier(2500, -100, 3),
    new Barrier(3100, -100, 2),
    new Barrier(3800, 350, 3),
    new Barrier(5350, 400, 1),
    new Barrier(6000, 0, 2),
    new Barrier(7200, 400, 0),
    new Barrier(7400, -100, 1),
  ];

  /**
   * Background layers with parallax factors
   * parallax: 0 = static, 1 = moves with camera, 0.5 = half speed, etc.
   */
  backgroundLayers = [
    // Far background - slowest parallax
    {
      parallax: 0.2,
      images: [
        { path: "./assets/landscape/bg/1.png", position: 0 },
        { path: "./assets/landscape/bg/2.png", position: 1920 },
      ],
    },
    // Middle background
    {
      parallax: 0.5,
      images: [
        { path: "./assets/landscape/bg-0/1.png", position: 0 },
        { path: "./assets/landscape/bg-0/2.png", position: 1920 },
      ],
    },
    // Light layer
    {
      parallax: 0.5,
      images: [
        { path: "./assets/landscape/light/1.png", position: 0 },
        { path: "./assets/landscape/light/2.png", position: 1920 },
      ],
    },
    // Near background
    {
      parallax: 0.8,
      images: [
        { path: "./assets/landscape/bg-1/1.png", position: 0 },
        { path: "./assets/landscape/bg-1/2.png", position: 1920 },
      ],
    },
    // Floor - moves with camera
    {
      parallax: 1.0,
      images: [
        { path: "./assets/landscape/floor/1.png", position: 0 },
        { path: "./assets/landscape/floor/2.png", position: 1920 },
      ],
    },
  ];

  // Legacy compatibility - flatten for existing code
  backgroundFiles = this.backgroundLayers.flatMap((layer) =>
    layer.images.map((img) => ({ ...img, parallax: layer.parallax }))
  );
}
