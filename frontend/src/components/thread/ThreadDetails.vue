<template>
			<div class="flex flex-col sm:flex-row bg-gradient-to-br bg-gray-50 border w-full rounded-xl">
				<div class="flex sm:flex-col justify-between gap-8 sm:rounded-l-xl w-full sm:w-28 bg-gray-100 px-2 py-1 sm:py-3">
					<div class="flex sm:flex-col gap-2 items-center w-full justify-between sm:justify-center">

						<div class="flex flex-col justify-center items-center">
							<p class="text-blue-500 font-semibold"> {{threadDetails.user__username}}  </p>
							<p class="text-xs text-gray-700 font-semibold">  {{threadDetails.user__date_joined}} </p>
						</div>
						</div>
						<div class="flex flex-col hidden sm:flex items-center justify-center">
							<button><i class="fas fa-caret-up text-gray-700 fa-2x" :class="{'text-green-400 cursor-not-allowed': true}"></i></button>
								<p class="text-gray-800 font-semibold leading-none" x-text="post.upvote - post.downvote"></p>
							<button ><i class="fas fa-caret-down text-gray-700 fa-2x" :class="{'text-green-400 cursor-not-allowed': false}"></i></button>
						</div>
					</div>
					<div class="flex flex-col gap-1.5 w-full justify-between">
						<div class="flex items-center justify-start px-2 py-1">
							<p class="text-xs text-gray-800 font-semibold"></p>
						</div>
						<div class="flex px-2 items-center justify-start">
							<h2 class="text-2xl text-gray-800 leading-none font-semibold">{{ threadDetails.title }}</h2>
						</div>
						<div class="flex px-2 justify-start">
							<p class="text-gray-700 leading-none">{{ threadDetails.desc }}</p>
						</div>
						<div class="flex overflow-y-hidden py-3 px-2 flex-col">
								
									
								
							<div class="flex gap-1 items-center justify-center">

									
							</div>			

						</div>
						<div class="flex px-2 py-1.5 justify-between w-full">
							<div class="flex sm:hidden gap-3 items-center justify-center">
								<button><i class="fas fa-caret-up text-gray-800 fa-2x"></i></button>
									<p class="text-gray-700 font-semibold leading-none"></p>
								<button><i class="fas fa-caret-down text-gray-800 fa-2x"></i></button>
							</div>
							<div class="flex gap-4 items-center justify-center">
								<button class="text-gray-800 flex items-center gap-0.t text-sm font-semibold"><svg class="w-5 h-5 text-gray-800" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M5 4a2 2 0 012-2h6a2 2 0 012 2v14l-5-2.5L5 18V4z"></path></svg> Save</button>								
							</div>
							<button>
								<svg class="w-5 h-5 text-gray-800" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path></svg>
							</button>
						</div>						
					</div>
				
			</div>
</template>

<script>
	export default {
		props: ['threadDetails']
	}
</script>