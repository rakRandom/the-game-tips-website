<script>
    import RedirectButton from "../RedirectButton.svelte";

    export let gameTitle = "MULTIVERSUS";
    export let description = "a";
    export let categoryPage = "";
</script>

<div class="w-full h-[567px] bg-[#00141E]">
    <div class="max-w-[1024px] h-full mx-auto pt-[52px] pb-[100px]">
        <div class="flex gap-[30px] h-full w-full">
            <div class="flex flex-col gap-4 w-[300px]">
                <h2 class="uppercase  text-[38px] text-[#2EC4B6] break-words">
                    {gameTitle}
                </h2>
                <p class="flex-1 text-lg text-ellipsis overflow-hidden">
                    {description}
                </p>
                <RedirectButton href={categoryPage} />
            </div>
            <div class="flex-1 h-full bg-white">

            </div>
        </div>
        <!-- Botõeszinhos de mudar o carrossel devem estar aqui :D -->
    </div>
</div>

<style>
  
</style>
