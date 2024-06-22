<script>
    export let className = "";
    export let title;
    export let seeAllPage;
    export let elementType;
    export let contents = [{}];
</script>

<div class="w-full h-fit {className}">
    <div class="max-w-[1024px] px-[16px] xl:px-[0px] h-full mx-auto">
        <div class="flex text-color-title">
            <h2 class="text-[24px] font-medium">
                {title}
            </h2>
            <a href={seeAllPage} class="ml-auto">
                <span class="hover:underline">See All</span> &#x279C;
            </a>
        </div>
        <div class="flex gap-4 justify-between mt-8 overflow-x-auto">
            {#each contents as content}
                <svelte:component this={elementType} {...content}/>
            {/each}
        </div>
    </div>
</div>

<style>
  
</style>
