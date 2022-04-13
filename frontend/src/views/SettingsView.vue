<template>
    <div class="flex flex-col max-w-sm bg-gray-50 py-3 px-6 rounded-xl shadow-sm gap-5">
        <div class="flex flex-col gap-1.5">
            <label class="font-semibold text-gray-800">Name</label>
            <input type="text" class="py-1 px-3 border rounded-lg">
            <button class="py-1.5 self-start px-4 bg-blue-500 hover:bg-blue-600 rounded-lg text-white text-sm font-semibold">Change name</button>
        </div>

        <div class="flex flex-col gap-1.5">
            <label class="font-semibold text-gray-800">Password</label>
            <button class="py-1.5 self-start px-4 bg-blue-500 hover:bg-blue-600 rounded-lg text-white text-sm font-semibold">Change Password</button>
        </div>
    </div>
</template>