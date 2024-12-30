
// components/course/LessonList.vue
<template>
  <div class="space-y-4">
    <div v-for="(lesson, index) in lessons" :key="lesson.id" class="bg-white rounded-lg shadow">
      <!-- Lesson Header -->
      <div 
        @click="toggleLesson(index)"
        class="p-4 flex items-center justify-between cursor-pointer"
      >
        <div class="flex items-center">
          <div class="flex-shrink-0 h-8 w-8 rounded-full bg-indigo-100 flex items-center justify-center">
            <span class="text-sm font-medium text-indigo-600">{{ index + 1 }}</span>
          </div>
          <div class="ml-4">
            <h4 class="text-lg font-medium text-gray-900">{{ lesson.title }}</h4>
            <p class="text-sm text-gray-500">{{ lesson.duration }} minutes</p>
          </div>
        </div>
        <ChevronDownIcon 
          class="h-5 w-5 text-gray-400 transform transition-transform duration-200"
          :class="{ 'rotate-180': openLessons[index] }"
        />
      </div>

      <!-- Lesson Content -->
      <div v-show="openLessons[index]" class="border-t border-gray-200 p-4">
        <div class="prose max-w-none">
          {{ lesson.content }}
        </div>
        
        <!-- Lesson Resources -->
        <div v-if="lesson.resources && lesson.resources.length" class="mt-4">
          <h5 class="text-sm font-medium text-gray-700 mb-2">Resources</h5>
          <ul class="space-y-2">
            <li v-for="resource in lesson.resources" :key="resource.id">
              <a 
                :href="resource.url"
                class="flex items-center text-sm text-indigo-600 hover:text-indigo-800"
              >
                <DocumentIcon class="h-4 w-4 mr-2" />
                {{ resource.name }}
              </a>
            </li>
          </ul>
        </div>

        <!-- Action Buttons -->
        <div class="mt-4 flex justify-end space-x-3">
          <button
            @click="$emit('edit', lesson)"
            class="px-3 py-1 text-sm text-indigo-600 bg-indigo-50 rounded hover:bg-indigo-100"
          >
            Edit
          </button>
          <button
            @click="$emit('delete', lesson)"
            class="px-3 py-1 text-sm text-red-600 bg-red-50 rounded hover:bg-red-100"
          >
            Delete
          </button>
        </div>
      </div>
    </div>

    <!-- Add Lesson Button -->
    <button
      @click="$emit('add')"
      class="w-full p-4 text-center border-2 border-dashed border-gray-300 rounded-lg text-gray-600 hover:border-indigo-500 hover:text-indigo-500"
    >
      <PlusIcon class="h-5 w-5 inline-block mr-2" />
      Add New Lesson
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { ChevronDownIcon, DocumentIcon, PlusIcon } from '@heroicons/vue/24/outline'

const props = defineProps({
  lessons: {
    type: Array,
    required: true
  }
})

defineEmits(['edit', 'delete', 'add'])

const openLessons = ref({})

const toggleLesson = (index) => {
  openLessons.value[index] = !openLessons.value[index]
}
</script>

// components/course/QuizForm.vue
<template>
  <div class="space-y-6">
    <!-- Quiz Settings -->
    <div class="bg-white p-6 rounded-lg shadow">
      <h3 class="text-lg font-medium text-gray-900 mb-4">Quiz Settings</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label class="block text-sm font-medium text-gray-700">Time Limit (minutes)</label>
          <input 
            v-model.number="quizData.timeLimit"
            type="number"
            min="0"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
          />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700">Passing Score (%)</label>
          <input 
            v-model.number="quizData.passingScore"
            type="number"
            min="0"
            max="100"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
          />
        </div>
      </div>
    </div>

    <!-- Questions -->
    <div class="space-y-4">
      <div v-for="(question, qIndex) in quizData.questions" :key="qIndex" class="bg-white p-6 rounded-lg shadow">
        <!-- Question Header -->