<template>
  <canvas ref="canvasEl" class="stars-background" aria-hidden="true"></canvas>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'

const props = withDefaults(
  defineProps<{
    factor?: number
    speed?: number
    starColor?: string
  }>(),
  {
    factor: 0.05,
    speed: 50,
    starColor: '#ffffff',
  },
)

type Star = {
  x: number
  y: number
  radius: number
  alpha: number
  layer: number
  phase: number
  solid: boolean
}

const canvasEl = ref<HTMLCanvasElement | null>(null)
let animationFrame = 0
let resizeObserver: ResizeObserver | undefined
let stars: Star[] = []
let width = 0
let height = 0
let pixelRatio = 1
let reducedMotion = false
let startTime = 0

const randomBetween = (min: number, max: number) => min + Math.random() * (max - min)

const createStar = (): Star => {
  const layer = Math.random()
  const solid = Math.random() < 0.12

  return {
    x: Math.random() * width,
    y: Math.random() * height,
    radius: solid ? randomBetween(0.85, 1.45) : randomBetween(0.65, 1.85) + layer * 0.35,
    alpha: solid ? 1 : randomBetween(0.16, 0.56) + layer * 0.18,
    layer,
    phase: Math.random() * Math.PI * 2,
    solid,
  }
}

const resetStars = () => {
  const area = Math.max(1, width * height)
  const quantity = Math.round((area / 720) * props.factor)
  stars = Array.from({ length: Math.max(42, Math.min(180, quantity)) }, createStar)
}

const resize = () => {
  const canvas = canvasEl.value
  if (!canvas) return

  const rect = canvas.getBoundingClientRect()
  width = rect.width
  height = rect.height
  pixelRatio = Math.min(window.devicePixelRatio || 1, 2)
  canvas.width = Math.max(1, Math.floor(width * pixelRatio))
  canvas.height = Math.max(1, Math.floor(height * pixelRatio))
  canvas.style.width = `${width}px`
  canvas.style.height = `${height}px`
  resetStars()
}

const draw = (time = 0) => {
  const canvas = canvasEl.value
  const ctx = canvas?.getContext('2d')
  if (!canvas || !ctx || !width || !height) return

  ctx.clearRect(0, 0, canvas.width, canvas.height)
  ctx.save()
  ctx.scale(pixelRatio, pixelRatio)

  const elapsed = reducedMotion ? 0 : Math.max(0, (time - startTime) / 1000)

  stars.forEach((star) => {
    const parallax = 0.22 + star.layer * 0.78
    const xDrift = Math.sin(elapsed * (0.34 + star.layer * 0.5) + star.phase) * (3 + star.layer * 8)
    const x = (star.x + xDrift + width) % width
    const y = ((star.y - elapsed * props.speed * parallax) % height + height) % height
    const pulse = star.solid ? 1 : 0.9 + Math.sin(elapsed * 0.9 + star.phase) * 0.1
    const alpha = Math.max(0, Math.min(1, star.alpha * pulse))

    ctx.globalAlpha = alpha
    ctx.fillStyle = props.starColor
    ctx.beginPath()
    ctx.arc(x, y < 0 ? y + height : y, star.radius, 0, Math.PI * 2)
    ctx.fill()
  })

  ctx.restore()
  animationFrame = window.requestAnimationFrame(draw)
}

onMounted(() => {
  reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  startTime = performance.now()
  resizeObserver = new ResizeObserver(resize)
  if (canvasEl.value) {
    resizeObserver.observe(canvasEl.value)
  }
  resize()
  animationFrame = window.requestAnimationFrame(draw)
})

onUnmounted(() => {
  window.cancelAnimationFrame(animationFrame)
  resizeObserver?.disconnect()
})
</script>

<style scoped>
.stars-background {
  display: block;
  width: 100%;
  height: 100%;
}
</style>
