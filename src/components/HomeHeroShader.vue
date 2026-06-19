<template>
  <div ref="shaderRoot" class="home-hero-shader" aria-hidden="true"></div>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'
import { createElement } from 'react'
import { createRoot, type Root } from 'react-dom/client'
import { ShaderGradient, ShaderGradientCanvas } from '@shadergradient/react'

const shaderRoot = ref<HTMLDivElement | null>(null)
let reactRoot: Root | undefined
const ShaderGradientElement = ShaderGradient as any
const ShaderGradientCanvasElement = ShaderGradientCanvas as any

onMounted(() => {
  if (!shaderRoot.value) return

  reactRoot = createRoot(shaderRoot.value)
  reactRoot.render(
    createElement(
      ShaderGradientCanvasElement,
      {
        className: 'home-hero-shader__canvas',
        fov: 45,
        pixelDensity: 1,
        pointerEvents: 'none',
        preserveDrawingBuffer: false,
        powerPreference: 'high-performance',
        lazyLoad: false,
        style: {
          position: 'absolute',
          inset: 0,
          width: '100%',
          height: '100%',
        },
      },
      createElement(ShaderGradientElement, {
        animate: 'on',
        axesHelper: 'off',
        bgColor1: '#000000',
        bgColor2: '#000000',
        brightness: 0.8,
        cAzimuthAngle: 270,
        cDistance: 0.5,
        cPolarAngle: 180,
        cameraZoom: 15.09,
        color1: '#0F1117',
        color2: '#0c7020',
        color3: '#064711',
        destination: 'onCanvas',
        embedMode: 'off',
        envPreset: 'city',
        format: 'gif',
        fov: 45,
        frameRate: 10,
        gizmoHelper: 'hide',
        grain: 'on',
        lightType: 'env',
        pixelDensity: 1,
        positionX: -0.1,
        positionY: 0,
        positionZ: 0,
        range: 'disabled',
        rangeEnd: 40,
        rangeStart: 0,
        reflection: 0.4,
        rotationX: 0,
        rotationY: 130,
        rotationZ: 70,
        shader: 'defaults',
        type: 'sphere',
        uAmplitude: 3.2,
        uDensity: 0.8,
        uFrequency: 5.5,
        uSpeed: 0.3,
        uStrength: 0.3,
        uTime: 0,
        wireframe: false,
      }),
    ),
  )
})

onUnmounted(() => {
  reactRoot?.unmount()
})
</script>

<style scoped>
.home-hero-shader {
  position: absolute;
  inset: 0;
  z-index: 0;
  overflow: hidden;
  pointer-events: none;
}
</style>
