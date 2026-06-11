<template>
  <canvas ref="canvasEl" class="hero-particles" />
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'

const props = withDefaults(
  defineProps<{
    quantity?: number
    ease?: number
    color?: string
    staticity?: number
  }>(),
  {
    quantity: 120,
    ease: 90,
    color: '#6ee7b7',
    staticity: 16,
  },
)

type Particle = {
  x: number
  y: number
  vx: number
  vy: number
  radius: number
  alpha: number
  pulse: number
  hueShift: number
}

const canvasEl = ref<HTMLCanvasElement>()
let animationFrame = 0
let resizeObserver: ResizeObserver | undefined
let particles: Particle[] = []
let width = 0
let height = 0
let pixelRatio = 1
let reducedMotion = false

const randomBetween = (min: number, max: number) => min + Math.random() * (max - min)

const createParticle = (): Particle => ({
  x: Math.random() * width,
  y: Math.random() * height,
  vx: randomBetween(-0.08, 0.08) / Math.max(1, props.staticity / 10),
  vy: randomBetween(-0.06, 0.06) / Math.max(1, props.staticity / 10),
  radius: randomBetween(0.8, 2.2),
  alpha: randomBetween(0.2, 0.78),
  pulse: randomBetween(0, Math.PI * 2),
  hueShift: randomBetween(0, 1),
})

const resetParticles = () => {
  particles = Array.from({ length: props.quantity }, createParticle)
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
  resetParticles()
}

const draw = (time = 0) => {
  const canvas = canvasEl.value
  const ctx = canvas?.getContext('2d')
  if (!canvas || !ctx || !width || !height) return

  ctx.clearRect(0, 0, canvas.width, canvas.height)
  ctx.save()
  ctx.scale(pixelRatio, pixelRatio)

  const drift = reducedMotion ? 0 : Math.max(0.12, props.ease / 420)
  const baseGradient = ctx.createLinearGradient(0, 0, width, height)
  baseGradient.addColorStop(0, props.color)
  baseGradient.addColorStop(0.52, '#35d5cf')
  baseGradient.addColorStop(1, '#62a9ff')

  particles.forEach((particle) => {
    if (!reducedMotion) {
      particle.x += particle.vx * drift
      particle.y += particle.vy * drift

      if (particle.x < -8) particle.x = width + 8
      if (particle.x > width + 8) particle.x = -8
      if (particle.y < -8) particle.y = height + 8
      if (particle.y > height + 8) particle.y = -8
    }

    const pulse = 0.72 + Math.sin(time * 0.0014 + particle.pulse) * 0.28
    const radius = particle.radius * pulse
    const alpha = particle.alpha * (0.56 + particle.hueShift * 0.38)

    ctx.globalAlpha = alpha
    ctx.fillStyle = baseGradient
    ctx.beginPath()
    ctx.arc(particle.x, particle.y, radius, 0, Math.PI * 2)
    ctx.fill()
  })

  ctx.restore()

  if (!reducedMotion) {
    animationFrame = window.requestAnimationFrame(draw)
  }
}

onMounted(() => {
  reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  resize()
  const canvas = canvasEl.value
  if (canvas) {
    resizeObserver = new ResizeObserver(resize)
    resizeObserver.observe(canvas)
  }
  draw()
})

onUnmounted(() => {
  if (animationFrame) {
    window.cancelAnimationFrame(animationFrame)
  }
  resizeObserver?.disconnect()
})
</script>
