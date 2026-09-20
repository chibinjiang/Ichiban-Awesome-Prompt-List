---
id: prompt-character-ai-fashion-commercial-street-photography-001
name: 服装图生图｜商业他拍超写实生活化上装
category: character
version: 1.0.0
status: experimental
language: zh-CN
tags:
  - fashion
  - image-to-image
  - clothing
  - commercial-photography
  - street-photography
  - photorealistic
  - product-display
  - model-photography
  - apparel
  - ai-image-generation
goal: 基于服装参考图生成真实、自然、生活化的商业他拍模特上装图片，突出参考服装的版型、材质和穿着效果。
use_cases:
  - 电商服装视觉生成
  - 服装上身效果图
  - 商业街拍风格模特图
  - 服装款式与搭配展示
non_use_cases:
  - 纯平铺服装展示
  - 对镜自拍风格
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
  - name: pose
    description: 人物姿势
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
  - 商业他拍视角
  - 模特真实穿着参考服装
  - 生活化、超写实摄影质感
  - 合理复杂的真实环境
  - 不出现手机、重复人物及可读文字
---

# 服装图生图｜商业他拍超写实生活化上装

## Prompt

```text
参考图是一件{category};

请从旁观者的角度, 生成一位时尚的小麦色皮肤的{country}白人女性少妇{when}在{where}上随意摆拍的正面照片:
人物姿势是{pose};

核心视觉要求: 超写实胶片颗粒感，暖调古铜色皮肤，伪纪实抓拍感，无过度AI塑料感; 双眼对称锐利对焦，瞳孔有自然反光，清透晒后妆，浅裸色唇色，拒绝深唇;

要求人物穿着参考图中的{category}, 并尽可能准确保留参考服装的款式、颜色、图案、材质、版型、领口、袖型、长度和关键设计细节;
要求人物的服装结构符合真实人体穿着逻辑，避免改变服装原有设计;
并合理搭配与{category}颜色不同的其它衣着搭配, 比如参考图中没有鞋子时请合理搭配跟衣服颜色不同的鞋子;
要求生成{num}张不同{where}场景的图片;
要求{where}场景复杂且合理, {where}的元素繁多且合理;
要求人物和衣服的细节真实合理, 衣服表面有轻微且自然的穿着褶皱, 衣服跟身体自然贴合;
要求照片有真实感和磨砂感, 特别注意人物跟景深的比例合理;
要求{where}和人物的光影和谐合理;
{extra}
要求拍照风格贴近生活, 具有高端商业街拍和真实纪实摄影的视觉质感;
要求摄影机位来自旁观者/摄影师视角，而不是镜面自拍或手机自拍视角;
要求人物身体比例、四肢、手指、五官和服装结构自然真实，不出现明显AI生成痕迹;
要求服装作为画面核心商品保持清晰、完整且容易辨认，同时人物与环境保持自然关系;
要求禁止出现牌匾/英文字母/中文汉字;
禁止出现重复的人物, 禁止出现手机.
```

## 使用说明

1. 该 Prompt 用于**服装参考图 → 模特商业他拍图**，服装参考图应作为主要视觉条件输入。
2. `{category}`、`{country}`、`{when}`、`{where}`、`{pose}`、`{num}`、`{extra}` 均来自 `ai-fashion-image-intent-parser` 的结构化输出。
3. 推荐先调用 `ai-fashion-image-intent-parser` 完成用户意图识别，再将其输出变量注入本 Prompt。
4. `{category}` 不应由用户随意填写，应优先依据参考图片识别，以减少服装分类错误。
5. `{where}` 应尽量具体，例如“巴黎街头咖啡馆门口”优于“街道”，这样更容易获得具有真实空间关系的商业街拍效果。
6. `{extra}` 用于承载用户额外要求，例如镜头焦段、构图比例、发型、配饰、天气、摄影风格等；没有额外要求时可以为空。
7. `num` 控制最终生成数量。如果底层工作流对批量生成有独立参数，应同时将该值传递给工作流。
8. 如果服装参考图包含多件服装，应确保 `{category}` 与参考图中的实际组合保持一致，并避免模型擅自替换核心服装。
9. 该 Prompt 强调“商业他拍”而非“自拍”：画面应表现为第三方摄影师从自然视角拍摄人物。
10. 如果模型对复杂场景中的服装细节还原能力不足，应优先保证服装主体、版型和关键设计元素，再增加环境复杂度。

## Evaluation Checklist

- [ ] 是否准确识别并保留参考服装的款式和关键设计？
- [ ] 是否为第三方旁观者/摄影师视角，而非自拍？
- [ ] 模特、服装和环境是否具有真实摄影关系？
- [ ] 服装是否自然贴合人体并具有合理褶皱？
- [ ] 人物身体比例、手指、五官是否自然？
- [ ] 是否具有真实胶片颗粒和生活化摄影质感？
- [ ] 光线、人物和背景景深是否协调？
- [ ] 场景是否复杂但具有真实空间逻辑？
- [ ] 是否避免手机、重复人物和可读文字？
- [ ] 是否避免明显AI塑料感？
- [ ] 多张图片之间是否保持服装主体一致，同时具有合理场景变化？

## Changelog

### 1.0.0
- 将用户提供的商业服装他拍模板整理为可复用 Prompt Card。
- 增加服装细节保持、摄影视角、人体结构、商业展示和评估标准。
