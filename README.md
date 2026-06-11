# Grid Beam Vue 3 组件

这是一个从 React/Framer Motion 转换而来的 Vue 3 版本的背景栅格光束组件。

## 安装依赖

```bash
npm install
# 或
pnpm install
# 或
yarn install
```

## 运行项目

```bash
npm run dev
```

默认会监听 `0.0.0.0`，同一局域网内的其他设备可以通过你的电脑局域网 IP 访问，例如：

```bash
http://192.168.1.88:3000
```

## 使用方法

### 基础用法

```vue
<template>
  <GridBeam>
    <div class="relative w-full h-full p-16">
      <h1 class="text-5xl font-bold">你的标题</h1>
      <p class="text-neutral-500">你的描述文本</p>
    </div>
  </GridBeam>
</template>

<script setup>
import GridBeam from './GridBeam.vue'
</script>
```

### 自定义类名

```vue
<GridBeam className="custom-class">
  <!-- 你的内容 -->
</GridBeam>
```

## 特性

- ✅ 完全保留原始视觉效果
- ✅ 纯 CSS 动画,无需第三方动画库
- ✅ 支持暗色模式
- ✅ 响应式设计
- ✅ TypeScript 支持

## 动画参数

光束动画使用 CSS @keyframes 实现:
- 持续时间: 1.8秒
- 延迟: 2秒
- 重复: 无限循环
- 缓动函数: linear

## 颜色渐变

光束使用三色渐变:
- 起始: 青色 (#18CCFC)
- 中间: 紫色 (#6344F5)
- 结束: 粉紫色 (#AE48FF)

## 文件结构

```
.
├── GridBeam.vue      # 主容器组件
├── Beam.vue          # SVG 光束组件
├── demo.vue          # 使用示例
├── tailwind.config.js # Tailwind 配置
└── package.json      # 项目依赖
```

## 注意事项

1. 确保已安装 TailwindCSS
2. 需要在 Tailwind 配置中添加 bg-grid 插件
3. 组件使用了 Composition API
