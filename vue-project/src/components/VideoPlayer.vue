<template>
  <div>
    <video v-if="videoReady" controls>
      <source :src="videoSrc" :type="videoType" cross-origin="anonymous" />
    </video>
    <span v-else> Error loading video </span>
  </div>
</template>

<script>
export default {
  data() {
    return {
      videoSrc: 'https://media.xiph.org/mango/tears_of_steel_1080p.webm',
      videoType: '',
    }
  },
  computed: {
    videoReady: function () {
      return !!this.videoSrc && !!this.videoType
    },
  },
  watch: {
    videoSrc: {
      handler: function () {
        this.updateVideoType()
      },
    },
  },
  methods: {
    async updateVideoType() {
      const fetchResult = await fetch(this.videoSrc, { methods: 'HEAD' })
      this.videoType = fetchResult.headers.get('Content-Type')
    },
  },
}
</script>

<style scoped>
video {
  width: 100%;
}
</style>
