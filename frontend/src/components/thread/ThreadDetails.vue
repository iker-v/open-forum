<template>
			<div class="flex flex-col sm:flex-row bg-gradient-to-br bg-gray-50 border w-full rounded-xl">
				<div class="flex sm:flex-col justify-between gap-8 sm:rounded-l-xl w-full sm:w-28 bg-gray-100 px-2 py-1 sm:py-3">
					<div class="flex sm:flex-col gap-2 items-center w-full justify-between sm:justify-center">
						<div class="flex flex-col justify-center items-center">
							<p class="text-blue-500 font-semibold"> {{threadDetails.user__username}} </p>
							<p class="text-xs text-gray-700 font-semibold">  {{threadDetails.user__date_joined}} </p>
						</div>
						<ThreadRate 
							:uuid="threadDetails.uuid"
							:upvote="threadDetails.upvote"
							:downvote="threadDetails.downvote"
						/>
					</div>

				</div>
					<div class="flex flex-col py-2 gap-1.5 w-full">
						<div class="flex px-2 lg:px-4 items-center justify-start">
							<h2 class="text-2xl text-gray-800 break-all font-semibold">{{ threadDetails.title }}</h2>
						</div>
						<div class="flex px-2 lg:px-4 justify-start">
							<p class="text-gray-700 break-all">{{ threadDetails.desc }}</p>
						</div>					
					</div>
			</div>
</template>

<script>
	import ThreadRate from './ThreadRate.vue'

	export default {
		components: {
			ThreadRate
		},
		props: ['threadDetails']
	}
</script>