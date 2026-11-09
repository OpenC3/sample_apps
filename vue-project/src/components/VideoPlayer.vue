<template>
  <div>
    <video v-if="videoReady" controls>
      <source :src="videoSrc" :type="videoType" cross-origin="anonymous" />
    </video>
    <span v-else> Error loading video </span>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'

const videoSrc = ref('https://media.xiph.org/mango/tears_of_steel_1080p.webm')
const videoType = ref('')

const videoReady = computed(() => !!videoSrc.value && !!videoType.value)

async function updateVideoType() {
  const fetchResult = await fetch(videoSrc.value, { methods: 'HEAD' })
  videoType.value = fetchResult.headers.get('Content-Type')
}

watch(videoSrc, updateVideoType)
</script>

<style scoped>
video {
  width: 100%;
}
</style>
