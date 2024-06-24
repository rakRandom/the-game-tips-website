<script>
  import Header from "../components/Header.svelte";
</script>

<Header className="absolute top-0 left-0 z-10" />

<div class="w-full h-svh bg-color-0">
    <div class="flex items-center justify-center w-full h-full">
        <div class="w-fit h-fit p-10">
            <h1 class="text-5xl text-color-title font-title-medium select-none">
                404: This page does not exist!
            </h1>
            <p class="text-lg text-center text-color-body mt-4">
                Click
                <a href="/" class="hover:underline text-color-title">
                    here
                </a>
                to go back to the Landing Page.
            </p>
        </div>
    </div>
</div>
