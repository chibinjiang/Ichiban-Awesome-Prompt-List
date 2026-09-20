---
id: prompt-character-ai-fashion-front-camera-selfie-001
name: 服装图生图｜前置摄像头自拍超写实生活化上装
category: character
version: 1.0.0
status: experimental
language: zh-CN
tags:
  - fashion
  - image-to-image
  - clothing
  - front-camera-selfie
  - smartphone-photography
  - photorealistic
  - lifestyle-photography
  - apparel
  - fashion-ecommerce
  - ai-image-generation
goal: 基于服装参考图生成真实、自然、生活化的前置摄像头自拍风格女性上装图片，突出参考服装的款式、材质和真实穿着效果。
use_cases:
  - 电商服装视觉生成
  - 服装上身效果图
  - 前置摄像头自拍风格模特图
  - 生活化服装内容生成
non_use_cases:
  - 纯平铺服装展示
  - 商业摄影师他拍视角
  - 需要严格复制真实人物身份的场景
variables:
  - name: category
    description: 从服装参考图识别出的服装分类
    required: true
  - name: country
    description: 拍摄国家/人物地域设定
    required: true
  - name: when
    description: 拍摄时间，如白天、傍晚、夜晚
    required: true
  - name: where
    description: 拍摄场景
    required: true
  - name: num
    description: 生成图片数量
    required: true
  - name: extra
    description: 额外的用户生图要求
    required: false
model_agnostic: true
recommended_models: []
input_contract:
  - 一张或多张服装参考图
  - ai-fashion-image-intent-parser 输出的结构化变量
output_contract:
  - 前置摄像头自拍视角
  - 模特真实穿着参考服装
  - 超写实、生活化摄影质感
  - 合理复杂的真实环境
  - 不出现重复人物及可读文字
---

# 服装图生图｜前置摄像头自拍超写实生活化上装

## Prompt

```text
参考图是一件{category}.

请从前置摄像头的角度, 拍摄一位时尚的小麦色皮肤的{country}白人女性少妇{when}在{where}内穿着参考图中的{category}的自拍照;
要求{where}场景复杂且合理, {where}的元素繁多且合理;

核心视觉要求: 超写实胶片颗粒感，暖调古铜色皮肤，伪纪实抓拍感，无过度AI塑料感; 双眼对称锐利对焦，瞳孔有自然反光，清透晒后妆，浅裸色唇色，拒绝深唇;
要求人物穿着参考图中的{category}, 并尽可能准确保留参考服装的款式、颜色、图案、材质、版型、领口、袖型、长度和关键设计细节;
要求人物的服装结构符合真实人体穿着逻辑, 避免改变服装原有设计;
要求人物和衣服的细节真实合理, 衣服表面有轻微且自然的穿着褶皱, 衣服跟身体自然贴合;
要求照片有真实感和磨砂感;
要求{where}的光影和人物光影和谐合理;
{extra}
要求前置摄像头自拍具有真实手机摄影的空间关系和轻微自然镜头感, 但不要出现手机本体;
要求拍照风格贴近生活, 避免过度商业棚拍效果;
要求人物身体比例、四肢、手指、五官和服装结构自然真实, 不出现明显AI生成痕迹;
要求服装作为画面核心商品保持清晰、完整且容易辨认;
禁止出现重复的人物;
要求禁止出现牌匾/英文字母/中文汉字;
要求生成{num}张不同{where}布置的图片.
```

## 使用说明

1. 该 Prompt 用于**服装参考图 → 前置摄像头自拍风格模特上装图**，服装参考图应作为主要视觉条件输入。
2. `{category}`、`{country}`、`{when}`、`{where}`、`{num}`、`{extra}` 均来自 `ai-fashion-image-intent-parser` 的结构化输出。
3. 推荐先调用 `ai-fashion-image-intent-parser` 完成用户意图识别，再将其输出变量注入本 Prompt。
4. `{category}` 应优先依据服装参考图识别，不应让用户输入覆盖图片中已经明确的服装类别。
5. `{where}` 应尽量具体，例如“卧室窗边”“酒店浴室”“咖啡馆座位区”，以提高环境空间关系的真实性。
6. `{extra}` 用于承载用户额外要求，例如发型、配饰、构图比例、镜头感、天气和穿搭要求；没有额外要求时可以为空。
7. `num` 控制最终生成数量。如果底层工作流有独立批量参数，应同时传递该值。
8. 多张图片应保持参考服装的核心款式、颜色、图案和版型一致，同时允许 `{where}` 内的布置和取景存在合理变化。
9. 本 Prompt 的核心是“前置摄像头自拍”，画面应体现自拍镜头的近距离视角和真实手机摄影空间关系，但**禁止出现手机本体**。
10. 如果场景复杂度与服装细节还原发生冲突，应优先保证参考服装的主体、版型、颜色、材质和关键设计细节。
11. “自拍”只表示摄影机位和构图方式，不应自动加入镜面、镜子或他人拍摄视角，除非 `{extra}` 明确要求。

## Evaluation Checklist

- [ ] 是否准确识别并保留参考服装的款式和关键设计？
- [ ] 是否明确表现为前置摄像头自拍视角？
- [ ] 是否避免出现手机本体？
- [ ] 人物、服装和环境是否具有真实摄影关系？
- [ ] 服装是否自然贴合人体并具有合理褶皱？
- [ ] 人物身体比例、手指、五官是否自然？
- [ ] 是否具有真实胶片颗粒、磨砂感和生活化摄影质感？
- [ ] 光线、人物和背景是否协调？
- [ ] 场景是否复杂但具有真实空间逻辑？
- [ ] 是否避免重复人物和可读文字？
- [ ] 是否避免明显AI塑料感？
- [ ] 多张图片之间是否保持服装主体一致，同时具有合理布置变化？

## Changelog

### 1.0.0
- 将用户提供的前置摄像头自拍服装图生图模板整理为可复用 Prompt Card。
- 增加服装细节保持、自拍摄影机位、真实手机摄影空间关系和评估标准。
