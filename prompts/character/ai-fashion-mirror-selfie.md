---
id: prompt-character-ai-fashion-mirror-selfie-001
name: 服装图生图｜对镜自拍风格AI上装
category: character
version: 1.0.0
status: experimental
language: zh-CN
tags:
  - character
  - fashion
  - image-to-image
  - mirror-selfie
  - outfit-generation
  - photorealistic
  - smartphone-photography
  - commercial
  - full-body
  - clothing

goal: 基于用户上传的服装参考图，生成真实自然的全身镜对镜自拍风格模特上装图片。
use_cases:
  - 电商服装视觉素材生成
  - 服装参考图到真人模特效果图
  - AI服装上装与场景扩展
  - 对镜自拍风格服装展示
non_use_cases:
  - 改变参考服装核心设计、颜色或版型
  - 生成带明显品牌文字或商业标识的场景

variables:
  - name: category
    description: 由 ai-fashion-image-intent-parser 从参考图识别出的服装分类
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
  - name: pose
    description: 由意图识别器输出的人物姿势
    required: true
  - name: num
    description: 由意图识别器输出的生成图片数量
    required: true
  - name: extra
    description: 用户额外的拍摄、人物、服装或场景要求
    required: false

model_agnostic: false
recommended_models:
  - image-to-image model with reference-image conditioning
input_contract:
  - 一张或多张服装参考图
  - ai-fashion-image-intent-parser 输出的结构化字段
output_contract:
  - 保留参考服装的主要款式、颜色、材质和结构特征
  - 生成真实自然的全身镜自拍视觉
  - 手机、人物、镜子和环境空间关系合理
  - 避免文字、品牌标识和重复人物

design_principles:
  - reference-clothing-preservation
  - realistic-fashion-photography
  - mirror-selfie-composition
  - natural-lighting
  - realistic-human-anatomy
  - scene-consistency
  - negative-prompt-constraints

examples:
  - input: category=针织连衣裙, country=美国, when=白天, where=卧室, pose=自然站立, num=1
    output: 使用模板生成对应的对镜自拍服装效果图

known_failures:
  - 镜面反射与真实人物姿态不一致
  - 手机、手指或镜框结构异常
  - 全身镜尺寸比例错误
  - 参考服装颜色、版型或细节发生漂移
  - 场景中生成不必要的文字、招牌或品牌Logo

changelog:
  - version: 1.0.0
    date: 2026-09-20
    changes: 初始版本
---

# 服装图生图｜对镜自拍风格AI上装

## Prompt

```text
参考图是一件{category};
请生成一位时尚的小麦色皮肤的{country}白人女性少妇{when}在{where}单手拿着iPhone手机对着全身镜自拍的正面照片;
人物姿势是{pose};
要求人物穿着参考图中的{category};
并合理搭配与{category}颜色不同的其它衣着搭配，比如参考图中没有鞋子时请合理搭配跟衣服颜色不同的鞋子;
核心视觉要求: 超写实胶片颗粒感，暖调古铜色皮肤，伪纪实抓拍感，无过度AI塑料感; 双眼对称锐利对焦，瞳孔有反光，清透晒后妆，浅裸色唇色，拒绝深唇;
要求生成{num}张不同{where}场景的图片;
要求{where}场景复杂且合理，{where}的元素繁多且合理;
要求人物和衣服的细节真实合理，{category}有轻微的穿着褶皱，衣服跟身体自然贴合;
要求照片有真实感和磨砂感，特别注意人物跟景深的比例合理;
要求全身镜的宽度跟人相近，露出少许全身镜的边框;
要求{where}和人物的自然光影和谐合理;
{extra}
要求拍照风格贴近生活;
禁止出现重复的人物，禁止出现手机;
要求禁止出现牌匾/英文字母/中文汉字.
```

## 使用说明

1. 先使用 `ai-fashion-image-intent-parser` 解析用户的服装参考图和生图需求。
2. 将解析得到的 `Category / Country / When / Where / Pose / PicsNum / Extra` 分别映射到 `{category} / {country} / {when} / {where} / {pose} / {num} / {extra}`。
3. `category` 必须优先依据参考服装图识别，不应仅根据用户文字猜测。
4. `where` 应保持为具体且具有视觉空间的场景，例如卧室、咖啡厅、街道、更衣区等，避免使用过于抽象的场景名称。
5. `{pose}` 应与“单手持手机对着全身镜自拍”的构图兼容；如果姿势与自拍动作冲突，应优先保证手部、手机、镜面反射和身体姿态的空间逻辑。
6. `{extra}` 用于承载用户额外指定的服装搭配、构图、环境、人物或摄影要求；没有额外要求时可以为空。
7. 本 Prompt 中“禁止出现手机”是用于最终画面约束：虽然人物执行的是持手机对镜自拍动作，但最终生成图应避免手机本体异常暴露、重复、畸形或成为视觉主体；如果工作流要求保留自然自拍手机，则应由下游模型根据具体工作流解释该约束。
8. 多张图片生成时，应保持人物和参考服装的一致性，同时改变 `{where}` 内部的合理布置、构图细节或环境状态，而不是简单复制同一张图片。
9. 重点保持参考服装的核心视觉特征，不应因为场景、人物或搭配变化而随意修改服装颜色、主要版型、材质和结构。

## Evaluation Checklist

- [ ] 是否正确使用参考服装图并保持核心款式？
- [ ] `{category}` 是否来自服装参考图识别结果？
- [ ] 人物是否为成年女性？
- [ ] 是否形成自然的全身镜对镜自拍构图？
- [ ] 人物、手机、镜面反射和全身镜之间的空间关系是否合理？
- [ ] 全身镜宽度是否与人物比例合理，并露出少许边框？
- [ ] 是否保持自然的人体比例、手部和手指结构？
- [ ] 服装是否具有自然褶皱并与身体合理贴合？
- [ ] 场景是否复杂但具有真实空间逻辑？
- [ ] 光影是否与人物、镜面和环境保持一致？
- [ ] 是否避免重复人物？
- [ ] 是否避免异常文字、中文汉字、英文字符、牌匾和Logo？
- [ ] 多张图片之间是否具有合理的场景变化而不是简单复制？
- [ ] 是否避免明显的AI塑料感和不自然皮肤质感？
```

# update INDEX using existing generator if available; otherwise append row safely
python - <<'PY'
from pathlib import Path
p=Path('/mnt/data/Ichiban-Awesome-Prompt-List/INDEX.md')
s=p.read_text()
row='| `prompt-character-ai-fashion-mirror-selfie-001` | [服装图生图｜对镜自拍风格AI上装](prompts/character/ai-fashion-mirror-selfie.md) | character | character, fashion, image-to-image, mirror-selfie, outfit-generation, photorealistic, smartphone-photography, commercial, full-body, clothing | experimental | 1.0.0 |'
if 'prompt-character-ai-fashion-mirror-selfie-001' not in s:
    lines=s.splitlines()
    # insert after table separator if possible
    idx=None
    for i,line in enumerate(lines):
        if line.startswith('|---'):
            idx=i+1
            break
    if idx is not None:
        lines.insert(idx,row)
        s='\n'.join(lines)+'\n'
    else:
        s=s.rstrip()+'\n\n'+row+'\n'
    p.write_text(s)
PY
ls -l /mnt/data/Ichiban-Awesome-Prompt-List/prompts/character/ai-fashion-mirror-selfie.md /mnt/data/Ichiban-Awesome-Prompt-List/INDEX.md
