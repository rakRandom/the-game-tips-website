<script>
    import { fetchImage } from "../../api/api_connection";

    import RedirectButton from "../RedirectButton.svelte";

    export let gameTitle;
    export let description;
    export let categoryID;
    export let imgSrc;
</script>

<div class="w-full lg:max-h-[567px] bg-color-mid">
    <div class="max-w-[1024px] h-full mx-auto pt-[32px] md:pt-0 lg:pb-[32px] lg:pt-[32px] lg:px-[32px] xl:px-0">
        <div class="flex flex-col md:flex-row gap-[30px] h-full w-full">
            <div class="flex flex-col gap-4 w-fit md:w-[300px] md:max-h-[438px] lg:max-h-full px-[32px] md:pr-0 md:py-[32px] lg:px-0 lg:py-0">
                <h2 class="uppercase text-[38px] text-color-title font-title-medium break-words">
                    {gameTitle}
                </h2>
                <p class="flex-1 text-lg text-color-body text-ellipsis overflow-hidden">
                    {description}
                </p>
                <RedirectButton href={"#/category/" + categoryID} />
            </div>
            <div class="flex-1 flex items-center gap-10 h-full overflow-x-auto">
                <img src={fetchImage(imgSrc)} alt="" class="w-full bg-white object-cover aspect-[14/10] max-md:aspect-video max-lg:aspect-square lg:rounded-lg lg:h-full">
            </div>
        </div>
    </div>
</div>

<style>

</style>
