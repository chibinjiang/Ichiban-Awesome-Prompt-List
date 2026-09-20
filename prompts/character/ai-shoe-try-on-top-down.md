---
id: prompt-character-ai-shoe-try-on-top-down-001
name: 鞋子图生图｜后置摄像头近距离俯拍试穿
category: character
version: 1.0.0
status: experimental
language: zh-CN
tags:
  - footwear
  - shoe-try-on
  - image-to-image
  - top-down
  - rear-camera
  - photorealistic
  - fashion
  - product-display
  - lifestyle-photography

goal: 基于用户上传的鞋子参考图，生成真实自然的女性试穿鞋子后置摄像头俯拍图片，重点展示鞋子的穿着效果、版型、材质和与环境的关系。
use_cases:
  - 鞋子电商试穿展示
  - 鞋子图生图
  - 鞋款上脚效果展示
  - 近距离俯拍商品视觉素材
non_use_cases:
  - 改变参考鞋款核心设计
  - 生成人物正脸肖像
  - 添加品牌Logo或文字广告

variables:
  - name: category
    description: 由 ai-fashion-image-intent-parser 从参考图识别出的鞋子分类
    required: true
  - name: country
    description: 由意图识别器输出的拍摄国家/人物设定
    required: true
  - name: when
    description: 由意图识别器输出的拍摄时间
    required: true
  - name: where
    description: 由意图识别器输出的拍摄场景
    required: true
  - name: extra
    description: 用户指定的脚下地面、材质或环境元素，例如木地板、草地、地毯、沙滩等
    required: true
  - name: num
    description: 由意图识别器输出的生成图片数量
    required: true

model_agnostic: false
recommended_models:
  - image-to-image model with reference-image conditioning
input_contract:
  - 一张或多张鞋子参考图
  - ai-fashion-image-intent-parser 输出的结构化字段
output_contract:
  - 保留参考鞋子的款式、颜色、材质和关键结构
  - 生成自然真实的上脚试穿效果
  - 使用后置摄像头视角和近距离俯拍构图
  - 保持双脚、鞋子、地面和环境之间合理的空间关系

design_principles:
  - reference-shoe-preservation
  - realistic-footwear-fitting
  - natural-foot-anatomy
  - top-down-composition
  - rear-camera-photography
  - realistic-ground-contact
  - natural-lighting
  - lifestyle-photography

examples:
  - input: category=白色运动鞋, country=美国, when=白天, where=城市街道, extra=浅灰色石材地面, num=2
    output: 使用模板生成两张不同构图的鞋子近距离俯拍试穿图

known_failures:
  - 鞋子颜色或结构与参考图发生漂移
  - 鞋子没有正确穿在脚上
  - 脚趾、脚踝或腿部出现不自然的解剖结构
  - 左右鞋款不一致
  - 鞋底与地面接触关系错误
  - 俯拍角度不明显，生成普通平视照片
  - 鞋子比例过大或过小
  - 地面纹理与光影方向不一致
  - 图片中出现手机、品牌Logo或文字

changelog:
  - version: 1.0.0
    date: 2026-09-20
    changes: 初始版本
---

# 鞋子图生图｜后置摄像头近距离俯拍试穿

## Prompt

```text
参考图是一双{category}。
请使用后置摄像头的角度，生成一位{country}白人女性{when}在{where}穿着参考图中的{category}、踩在有{extra}的地面上，并近距离拍摄自己的脚部的{num}张俯拍图片。

要求以真实手机后置摄像头近距离俯拍的生活化摄影效果呈现，重点突出参考鞋子的真实上脚效果；
要求参考图中的{category}保持原有的颜色、款式、材质、鞋底结构、鞋带/装饰和主要设计细节，不得无理由改变鞋款；
要求鞋子自然穿在女性双脚上，鞋口、鞋面、脚背、脚踝与鞋子的接触关系符合真实穿着状态；
要求双脚和鞋子的比例自然，左右脚解剖结构合理，脚趾、脚踝和腿部不要出现畸形或重复；
要求鞋底与{extra}地面产生真实接触，重力、阴影、接触面积和透视关系符合真实物理效果；
要求{where}环境真实合理，背景元素与{extra}地面材质具有自然空间关系；
要求自然光影与鞋子、脚部和地面协调一致，避免悬浮、穿模或明显的AI合成感；
要求照片具有真实手机摄影的细节、轻微磨砂质感和自然景深，不要过度锐化或塑料感；
要求每张图片的俯拍构图、脚部位置和{where}背景布置存在合理差异，同时保持参考鞋款的一致性；
{extra}
禁止出现重复的人物、重复的脚或重复的鞋子；
禁止出现手机、镜子、自拍杆；
要求禁止出现牌匾、英文字母、中文汉字、Logo和品牌标识。
```

## 使用说明

1. 先使用 `ai-fashion-image-intent-parser` 解析用户上传的鞋子参考图和生图需求。
2. 将解析结果中的 `Category / Country / When / Where / Extra / PicsNum` 分别映射到 `{category} / {country} / {when} / {where} / {extra} / {num}`。
3. `{category}` 必须根据鞋子参考图识别，例如运动鞋、跑鞋、板鞋、乐福鞋、短靴、高跟鞋、凉鞋等，不应仅根据用户文字猜测。
4. `{extra}` 在本 Prompt 中承担“脚下环境/地面材质”的作用，例如木地板、浅色瓷砖、草地、沙滩、混凝土地面、地毯等。若原始意图识别器中的 `extra` 没有明确地面信息，应将用户提供的场景细节转换为适合鞋子俯拍的地面描述。
5. 构图核心是“后置摄像头 + 近距离 + 俯拍 + 脚部和鞋子为主体”，不应生成正面人物全身照或普通产品棚拍图。
6. 鞋子应真实穿在脚上，重点保持参考图鞋款的一致性，同时允许根据真实穿着状态产生合理的鞋面褶皱、压痕和自然形变。
7. 多张图片应改变俯拍角度、双脚位置和背景布置，但不能因此改变鞋子的颜色、结构和核心设计。
8. 如果参考图只展示单只鞋，应根据参考图合理生成对应的另一只鞋，但不得随意修改鞋款设计。
9. 应优先保持自然的脚部解剖结构和鞋子与脚的接触关系，避免多脚、多趾、脚趾融合、鞋子穿模和左右脚不一致。
10. 不应出现完整人物脸部；人物身份仅用于满足用户指定的人物设定，画面主体应始终是鞋子和脚部。
11. 最终图片不得出现手机本体、自拍杆、镜子、文字、Logo、品牌标识或广告牌。

## Evaluation Checklist

- [ ] 是否正确识别并保留参考鞋子的核心款式？
- [ ] `{category}` 是否来自鞋子参考图？
- [ ] 是否明确使用后置摄像头视角？
- [ ] 是否形成近距离俯拍构图？
- [ ] 鞋子是否真实穿在双脚上？
- [ ] 左右脚和脚趾解剖结构是否自然？
- [ ] 是否不存在多脚、多趾或重复鞋子？
- [ ] 鞋子颜色、材质、鞋底和关键设计是否与参考图一致？
- [ ] 鞋子与脚部是否具有真实接触和自然形变？
- [ ] 鞋底与地面是否具有合理接触阴影？
- [ ] `{extra}` 是否形成清晰且合理的脚下环境？
- [ ] `{where}` 是否与地面、光线和空间关系合理？
- [ ] 是否具有真实手机后置摄像头摄影质感？
- [ ] 是否避免明显AI塑料感、过度锐化和不自然景深？
- [ ] 多张图片是否具有合理的构图和背景变化？
- [ ] 是否禁止手机、镜子、自拍杆、中文、英文、Logo和品牌标识？
```
