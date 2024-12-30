// components/course/CourseCard.vue
<template>
  <div class="bg-white rounded-lg shadow-md overflow-hidden">
    <!-- Course Image -->
    <div class="relative h-48">
      <img 
        :src="course.thumbnail || '/api/placeholder/400/200'" 
        :alt="course.title"
        class="w-full h-full object-cover"
      >
      <div class="absolute top-2 right-2">
        <span 
          class="px-2 py-1 text-xs font-semibold rounded-full"
          :class="getStatusClass(course.status)"
        >
          {{ course.status }}
        </span>
      </div>
    </div>

    <!-- Course Content -->
    <div class="p-4">
      <div class="flex items-center justify-between mb-2">
        <span class="text-sm text-indigo-600 font-medium">{{ course.category }}</span>
        <div class="flex items-center">
          <ClockIcon class="h-4 w-4 text-gray-400 mr-1" />
          <span class="text-sm text-gray-500">{{ course.duration }}</span>
        </div>
      </div>

      <h3 class="text-lg font-semibold text-gray-900 mb-2">{{ course.title }}</h3>
      <p class="text-sm text-gray-600 mb-4 line-clamp-2">{{ course.description }}</p>

      <!-- Progress Bar (if enrolled) -->
      <div v-if="course.progress" class="mb-4">
        <div class="flex justify-between text-sm text-gray-600 mb-1">
          <span>Progress</span>
          <span>{{ course.progress }}%</span>
        </div>
        <div class="w-full bg-gray-200 rounded-full h-2">
          <div 
            class="bg-indigo-600 h-2 rounded-full" 
            :style="{ width: `${course.progress}%` }"
          ></div>
        </div>
      </div>

      <!-- Course Info -->
      <div class="flex items-center justify-between text-sm text-gray-500 mb-4">
        <div class="flex items-center">
          <UserGroupIcon class="h-4 w-4 mr-1" />
          {{ course.enrolledStudents }} students
        </div>
        <div class="flex items-center">
          <StarIcon class="h-4 w-4 text-yellow-400 mr-1" />
          {{ course.rating }}
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex space-x-2">
        <button 
          @click="$emit('edit', course)" 
          class="flex-1 px-4 py-2 text-sm font-medium text-indigo-600 bg-indigo-50 rounded-md hover:bg-indigo-100"
        >
          Edit Course
        </button>
        <button 
          @click="$emit('view', course)" 
          class="flex-1 px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-md hover:bg-indigo-700"
        >
          View Details
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ClockIcon, UserGroupIcon, StarIcon } from '@heroicons/vue/24/outline'

const props = defineProps({
  course: {
    type: Object,
    required: true
  }
})

defineEmits(['edit', 'view'])

const getStatusClass = (status) => {
  const classes = {
    'active': 'bg-green-100 text-green-800',
    'draft': 'bg-gray-100 text-gray-800',
    'archived': 'bg-red-100 text-red-800'
  }
  return classes[status.toLowerCase()] || 'bg-gray-100 text-gray-800'
}
</script>
