
// components/course/CourseForm.vue
<template>
  <form @submit.prevent="handleSubmit" class="space-y-6">
    <div class="bg-white p-6 rounded-lg shadow">
      <!-- Basic Information -->
      <h3 class="text-lg font-medium text-gray-900 mb-4">Basic Information</h3>
      <div class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700">Course Title</label>
          <input 
            v-model="formData.title"
            type="text"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            required
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Category</label>
          <select 
            v-model="formData.category"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
          >
            <option v-for="category in categories" :key="category" :value="category">
              {{ category }}
            </option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Description</label>
          <textarea 
            v-model="formData.description"
            rows="4"
            class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
          ></textarea>
        </div>

        <!-- Course Thumbnail -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Course Thumbnail</label>
          <div class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md">
            <div class="space-y-1 text-center">
              <div v-if="formData.thumbnail" class="mb-4">
                <img :src="formData.thumbnail" alt="Preview" class="mx-auto h-32 w-auto" />
              </div>
              <div class="flex text-sm text-gray-600">
                <label class="relative cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500">
                  <span>Upload a file</span>
                  <input type="file" class="sr-only" @change="handleThumbnailUpload" accept="image/*">
                </label>
              </div>
            </div>
          </div>
        </div>

        <!-- Course Settings -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-gray-700">Duration (hours)</label>
            <input 
              v-model.number="formData.duration"
              type="number"
              min="0"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700">Price</label>
            <div class="mt-1 relative rounded-md shadow-sm">
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <span class="text-gray-500 sm:text-sm">$</span>
              </div>
              <input 
                v-model.number="formData.price"
                type="number"
                min="0"
                step="0.01"
                class="pl-7 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
              />
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Action Buttons -->
    <div class="flex justify-end space-x-3">
      <button
        type="button"
        @click="$emit('cancel')"
        class="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50"
      >
        Cancel
      </button>
      <button
        type="submit"
        class="px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-md hover:bg-indigo-700"
      >
        Save Course
      </button>
    </div>
  </form>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({
  initialData: {
    type: Object,
    default: () => ({})
  }
})

const emit = defineEmits(['submit', 'cancel'])

const categories = [
  'Programming',
  'Design',
  'Business',
  'Marketing',
  'Personal Development'
]

const formData = ref({
  title: '',
  category: '',
  description: '',
  thumbnail: '',
  duration: 0,
  price: 0,
  ...props.initialData
})

const handleThumbnailUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      formData.value.thumbnail = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

const handleSubmit = () => {
  emit('submit', formData.value)
}

onMounted(() => {
  if (props.initialData) {
    formData.value = { ...formData.value, ...props.initialData }
  }
})
</script>
