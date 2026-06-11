<template>
  <div :class="cn('relative w-full h-full', className)">
    <Beam />
    <slot></slot>
  </div>
</template>

<script setup lang="ts">
import Beam from './Beam.vue'

interface Props {
  className?: string
}

defineProps<Props>()

// cn utility function
const cn = (...classes: (string | undefined)[]) => {
  return classes.filter(Boolean).join(' ')
}
</script>
