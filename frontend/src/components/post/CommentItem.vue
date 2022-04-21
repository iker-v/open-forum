<template>
    <div class="flex flex-col border-l-2 pl-2 py-1">
        <div class="flex items-end gap-2">
            <h3 class="text-blue-500 font-semibold"> @{{ co.user__username }} </h3>
            <p class="text-xs font-semibold py-0.5 text-gray-400"> {{ new Date(co.date).toLocaleDateString('en-us', { year: 'numeric', month: 'short', day: 'numeric' }) }} </p>
        </div>
        <div class="py-1">
            <p class="text-gray-900"> {{ co.comment }} </p>
        </div>
    </div>
</template>

<script>

    export default {
        props: ['co']
    }

</script>