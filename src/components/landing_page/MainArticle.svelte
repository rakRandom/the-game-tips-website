<script>
    import { fetchImage } from "./../../api/api_connection";
    import RedirectButton from "../RedirectButton.svelte";
    
    export let className = "";

    // IMG variables
    export let imgSrc;

    // Text variables
    export let gameName;
    export let categoryPage;
    export let articleTitle;
    // Todo: Author Image
    export let authorName;
    export let articleDate;
    export let authorPage;  // Redirection

    // Button variables
    export let articlePage;  // Redirection
</script>

<div class="bg-[#001A24] w-full h-[644px] {className}">
    <div class="flex gap-8 max-w-[1320px] h-full mx-auto py-20">
        <img src={fetchImage(imgSrc)} alt="" class="bg-white h-full aspect-video rounded-xl">
        <div class="flex flex-col w-full">
            <div class="flex-1">
                <a href={categoryPage} class="group text-[#69D3C9] text-[2.5rem] font-title-semibold uppercase cursor-pointer">
                    {gameName}
                    <hr class="w-0 transition-all delay-100 duration-1000 border-[1px] border-transparent group-hover:border-[#69D3C9] group-hover:w-full">
                </a>
                <p class="text-[1.75rem] mt-4">
                    {articleTitle}
                </p>
            </div>
            
            <div class="flex items-center w-full justify-between">
                <p class="text-[#69D3C9] text-[18px]">
                    By 
                    <a href={authorPage} class="hover:underline">
                        {authorName}
                    </a> 
                    | {articleDate}
                </p>

                <RedirectButton href={articlePage} />
            </div>
        </div>
    </div>
</div>

<style>
  
</style>
