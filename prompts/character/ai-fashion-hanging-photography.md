---
id: prompt-character-ai-fashion-hanging-photography-001
name: 服装图生图｜挂拍风格AI服装细节展示
category: character
version: 1.0.0
status: experimental
language: zh-CN
tags:
  - fashion
  - image-to-image
  - hanging-photography
  - clothing-detail
  - photorealistic
  - commercial-fashion
  - apparel
  - product-display
  - texture
  - lifestyle-photography

goal: 基于用户上传的服装参考图，生成真实自然的服装挂拍细节图片，用于展示服装材质、版型、褶皱和环境搭配。
use_cases:
  - 电商服装细节展示
  - 服装挂拍视觉素材生成
  - 服装材质与做工展示
  - 服装场景化商品图片生成
non_use_cases:
  - 生成人物穿着效果
  - 改变参考服装核心设计、颜色或材质
  - 生成品牌Logo、广告牌或商业文字

variables:
  - name: category
    description: 由 ai-fashion-image-intent-parser 从参考图识别出的服装分类
    required: true
  - name: when
    description: 由意图识别器输出的拍摄时间，例如白天、晚上
    required: true
  - name: where
    description: 由意图识别器输出的服装悬挂场景，例如卧室、衣帽间、阳台、店铺陈列区等
    required: true
  - name: num
    description: 由意图识别器输出的生成图片数量
    required: true
  - name: extra
    description: 用户额外指定的拍摄、服装、背景或构图要求
    required: false

model_agnostic: false
recommended_models:
  - image-to-image model with reference-image conditioning
input_contract:
  - 一张或多张服装参考图
  - ai-fashion-image-intent-parser 输出的结构化字段
output_contract:
  - 保留参考服装的主要款式、颜色、材质、结构和细节
  - 生成自然真实的服装挂拍视觉
  - 服装与悬挂环境具有合理的空间关系
  - 避免人物、手机、文字、品牌标识和重复主体

design_principles:
  - reference-clothing-preservation
  - realistic-clothing-texture
  - hanging-garment-composition
  - natural-lighting
  - realistic-material-folds
  - environmental-consistency
  - negative-prompt-constraints

examples:
  - input: category=针织开衫, when=白天, where=卧室, num=1
    output: 使用模板生成对应的服装挂拍细节图

known_failures:
  - 服装被错误生成在人体上
  - 衣架、挂钩或悬挂方式不符合真实物理结构
  - 服装材质和褶皱过度平滑，缺乏真实细节
  - 服装颜色、版型或局部结构发生漂移
  - 背景元素过少，导致画面像简单抠图
  - 场景光源方向与服装高光、阴影不一致
  - 背景中出现文字、Logo、牌匾或无意义字符

changelog:
  - version: 1.0.0
    date: 2026-09-20
    changes: 初始版本
---

# 服装图生图｜挂拍风格AI服装细节展示

## Prompt

```text
参考图是一件{category}。
请从近距离拍摄的角度，生成参考图的{category}{when}挂在{where}上的局部细节照片；
要求生成{num}张不同{where}背景的图片；
要求{where}和{category}的细节真实合理，{category}表面有轻微且自然的褶皱；
要求照片有真实感和磨砂感；
要求{where}和{category}的光影和谐合理；
要求拍照风格贴近生活；
{extra}
禁止出现人物，禁止出现重复的人物，禁止出现手机；
要求禁止出现牌匾/英文字母/中文汉字/Logo/品牌标识。
```

## 使用说明

1. 先使用 `ai-fashion-image-intent-parser` 解析用户上传的服装参考图和生图需求。
2. 将解析得到的 `Category / When / Where / PicsNum / Extra` 分别映射到 `{category} / {when} / {where} / {num} / {extra}`。
3. `{category}` 必须优先依据参考服装图识别，不应仅根据用户文字猜测；生成结果应尽量保持参考图中的颜色、版型、材质、纹理和关键结构。
4. `{where}` 应描述具有明确空间关系的真实场景，例如衣帽间、卧室、阳台、衣柜旁、门后、店铺陈列区等；避免过于抽象或无法实现服装悬挂的场景。
5. “挂拍”重点是展示服装本身，而不是人物穿着效果。服装应自然悬挂、平衡或依附于合理的衣架/挂钩/墙面结构，不应生成真人模特或人体轮廓。
6. 近距离构图应重点突出服装的材质、针脚、纹理、边缘、领口、袖口、纽扣、拉链等真实细节，但不得擅自添加参考图中不存在的重要设计元素。
7. 服装褶皱应符合重力、材质和悬挂方式产生的自然状态，避免完全笔直、塑料感、过度规则或夸张褶皱。
8. `{extra}` 用于承载用户额外指定的场景、背景、光线、构图、材质或展示要求；没有额外要求时可以为空。
9. 多张图片生成时，应保持同一件参考服装的核心视觉特征一致，同时改变 `{where}` 内合理的背景布置、环境细节或拍摄构图，不应简单复制同一张图片。
10. 背景应具有足够真实的环境细节，但不能抢夺服装主体的视觉注意力；服装与背景之间应有合理的景深关系。
11. 如果参考图本身包含衣架、挂钩或其他悬挂结构，应优先保持其合理结构；如果参考图没有，应根据场景生成自然、低存在感的悬挂方式。
12. 最终图片不得出现人物、手机、重复主体、牌匾、中文汉字、英文字符、Logo或品牌标识。

## Evaluation Checklist

- [ ] 是否正确使用参考服装图并保持核心款式？
- [ ] `{category}` 是否来自服装参考图识别结果？
- [ ] 是否明确表现为挂拍/悬挂状态，而不是人物穿着状态？
- [ ] 是否不存在人物、人体或重复人物？
- [ ] 衣服的悬挂方式是否符合真实物理结构？
- [ ] 服装材质、纹理、针脚和局部细节是否真实？
- [ ] 服装是否具有轻微且自然的重力褶皱？
- [ ] 服装颜色、版型和主要结构是否与参考图一致？
- [ ] `{where}` 是否具有真实、丰富且合理的环境细节？
- [ ] 背景是否不会抢夺服装主体的视觉注意力？
- [ ] 服装与背景的景深关系是否自然？
- [ ] 光源方向、阴影和服装高光是否一致？
- [ ] 是否具有真实摄影的磨砂质感和生活化风格？
- [ ] 是否避免明显的AI塑料感和过度锐化？
- [ ] 是否避免中文、英文、牌匾、Logo和品牌标识？
- [ ] 多张图片之间是否具有合理的场景变化？
```
