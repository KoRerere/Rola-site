<template>
  <div class="home-cobe-globe" aria-hidden="true">
    <canvas ref="canvasRef" class="home-cobe-globe__canvas"></canvas>
    <span class="home-cobe-globe__halo"></span>
    <span class="home-cobe-globe__orbit home-cobe-globe__orbit--one"></span>
    <span class="home-cobe-globe__orbit home-cobe-globe__orbit--two"></span>
  </div>
</template>

<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'
import createGlobe, { type Globe } from 'cobe'

const canvasRef = ref<HTMLCanvasElement | null>(null)
let globe: Globe | undefined
let frameId = 0
let resizeObserver: ResizeObserver | undefined
let phi = 0

const markers = [
  { location: [37.7749, -122.4194] as [number, number], size: 0.055 },
  { location: [40.7128, -74.006] as [number, number], size: 0.045 },
  { location: [51.5072, -0.1276] as [number, number], size: 0.05 },
  { location: [1.3521, 103.8198] as [number, number], size: 0.05 },
  { location: [35.6762, 139.6503] as [number, number], size: 0.045 },
]

const arcs = [
  { from: [37.7749, -122.4194] as [number, number], to: [51.5072, -0.1276] as [number, number] },
  { from: [51.5072, -0.1276] as [number, number], to: [1.3521, 103.8198] as [number, number] },
  { from: [40.7128, -74.006] as [number, number], to: [35.6762, 139.6503] as [number, number] },
]

const renderGlobe = () => {
  const canvas = canvasRef.value
  if (!canvas) {
    return
  }

  const rect = canvas.getBoundingClientRect()
  const size = Math.max(260, Math.round(Math.min(rect.width || 320, rect.height || 320)))
  const pixelRatio = Math.min(window.devicePixelRatio || 1, 2)

  canvas.width = size
  canvas.height = size

  globe?.destroy()
  globe = createGlobe(canvas, {
    devicePixelRatio: pixelRatio,
    width: size,
    height: size,
    phi,
    theta: 0.28,
    dark: 0.78,
    diffuse: 1.15,
    scale: 1.05,
    mapSamples: 14000,
    mapBrightness: 5.6,
    baseColor: [0.1, 0.22, 0.34],
    markerColor: [0.44, 0.96, 0.66],
    glowColor: [0.28, 0.82, 0.78],
    arcColor: [0.34, 0.92, 0.78],
    arcWidth: 0.7,
    arcHeight: 0.38,
    markerElevation: 0.03,
    markers,
    arcs,
    opacity: 0.98,
  })
}

const animate = () => {
  phi += 0.0038
  globe?.update({ phi })
  frameId = window.requestAnimationFrame(animate)
}

onMounted(() => {
  renderGlobe()
  resizeObserver = new ResizeObserver(renderGlobe)
  if (canvasRef.value) {
    resizeObserver.observe(canvasRef.value)
  }
  frameId = window.requestAnimationFrame(animate)
})

onBeforeUnmount(() => {
  window.cancelAnimationFrame(frameId)
  resizeObserver?.disconnect()
  globe?.destroy()
})
</script>
