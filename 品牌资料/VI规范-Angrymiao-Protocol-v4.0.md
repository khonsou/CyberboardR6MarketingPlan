# Angrymiao Protocol v4.0: AI-Visual Engine（用户提供原文存档）

### [Angrymiao Protocol v4.0: Visual Alchemy]  

# ID: [PROJ]-[SKU]-[PHASE]-[VER]  
# Date: 2024-XX-XX  
# Role Definition:  
# - Planner (策略脑): 定义商业目的、叙事角度、核心冲突。  
# - Designer (视觉脑): 负责 Prompt Engineering、光影逻辑、材质物理属性。  

# --- CORE CONTEXT (DO NOT MODIFY) ---  
# Brand: Angrymiao (怒喵)  
# Aesthetic: Future Art, Cyberpunk Luxury, Streetwear Tech.  
# Key Elements: Polycarbonate (Transparent), CNC Aluminum, LED Matrix, Graffiti, AM Monogram.  
# Target Audience: Global High-Net-Worth Gen Z (Hypebeast, Geek, Crypto-Rich).  

--- BLOCK A: 策略锚点 (Owner: Planner) ---  
# 定义这张图要解决的商业问题。  

[Campaign Theme]: (e.g., #RethinkV3P 尺寸盲测)  
[Hero Product]: (e.g., AM 65 Less, 冰川银配色, 侧面特写)  
[The Hook (第一眼视觉重心)]: (e.g., 聚焦在手指触摸键盘边缘的瞬间，强调金属的冷冽感)  
[Scenario (场景叙事)]: (e.g., 一个光线昏暗的极客桌面，只有屏幕挂灯和键盘底灯照亮，充满神秘感)  
[Output Channel]: (e.g., Instagram Story 9:16 - 需要上下留白放文字)  

--- BLOCK B: 视觉编译 (Owner: Designer 覆写) ---  
# 将策略翻译为物理渲染参数。  

[1. Composition & Camera]:  
# Planner 描述: (e.g., 很有压迫感，像电影大片)  
# Designer 重构: Low angle shot, macro photography, depth of field, f/1.8, focus on texture, cinematic composition.  

[2. Lighting & Mood]:  
# Planner 描述: (e.g., 冷冷的，像银翼杀手，有点紫色)  
# Designer 重构: Volumetric lighting, neon purple and cyan rim light, moody atmosphere, contrasty, ray tracing reflections.  

[3. Material & Texture]:  
# Planner 描述: (e.g., 看起来很贵，金属质感好，半透明)  
# Designer 重构: Brushed aluminum texture, frosted polycarbonate, sub-surface scattering (SSS), imperceptible scratches (adds realism), 8k textures.  

--- BLOCK C: 品牌DNA与防呆 (Owner: Designer) ---  
# 确保它是 Angry Miao，而不是 Razer 或 Logitech。  

[Brand Monogram Integration]:  
# 规则: 必须作为物理材质存在，而非后期贴图。  
# Prompting Strategy: "Laser etched Angrymiao monogram pattern on the metal surface" OR "LED matrix displaying pixel art cat logo".  

[Negative Constraints (Anti-Brand)]:  
# 绝对禁止出现:  
--no cartoon, illustration, low poly, warm cozy lighting, messy cables, cheap plastic, over-saturated, human faces (unless specified), cute style.  

[Tech Specs]:  
# 渲染引擎与质量:  
Unreal Engine 5 render, Octane render, hyper-realistic, 8k resolution.  
# Aspect Ratio (根据 Block A 自动调整):  
--ar [16:9 | 9:16 | 4:5] --v 6.0 --stylize 250  

--- OUTPUT GENERATION (Execution) ---  

# Action:   
1. Planner 填写 Block A。  
2. Designer 根据 Block A 填写 Block B & C。  
3. 将组合后的关键词输入 Midjourney / Stable Diffusion。  

# 最终提示词结构 (Example):  
/imagine prompt: [Block A: Scenario & Hero Product] + [Block B: Camera, Lighting, Material] + [Block C: Monogram] + [Block C: Tech Specs] + [Block C: Negative Constraints] + [Block C: AR]
