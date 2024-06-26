<script>
    import { fetchImage } from "./../../api/api_connection";
    
    export let className = "";

    // IMG variables
    export let imgSrc;

    // Text variables
    export let gameName;
    export let categoryID;
    export let articleTitle;
    // Todo: Author Image
    export let authorName;
    export let articleDate;
    export let authorPage;  // Redirection

    // Button variables
    export let articleID;  // Redirection
</script>

<div class="bg-[#E6F4F3] dark:bg-[#001A24] w-full h-fit {className}">
    <div class="flex flex-col gap-8 max-w-[1280px] mx-auto pb-10 lg:px-[96px] h-full">
        <a href={"#/article/" + articleID} class="aspect-video">
            <img src={fetchImage(imgSrc)} alt="" class="h-full w-full aspect-video object-cover lg:rounded-b-lg">
        </a>
        
        <div class="flex flex-col lg:flex-row gap-2 w-full px-[16px] lg:px-[32px]">
            <div class="w-full lg:w-[33%] text-color-title">
                <h2 class="group text-[2rem] font-title-medium uppercase mb-2 w-fit">
                    <a href={"#/category/" + categoryID}>
                        {gameName}
                    </a>
                    <hr class="hidden lg:block w-0 group-hover:w-full border-t-2 border-[#1E9B8F] dark:border-[#69D3C9] transition-all delay-200 duration-1000">
                </h2>
                <p class="text-[1rem] opacity-75 font-light">
                    By
                    <a href={"#/user/" + authorPage} class="hover:underline">
                        {authorName}
                    </a>
                    - {articleDate}
                </p>
            </div>
            <div class="flex items-center w-full lg:w-[66%] lg:px-4 lg:py-2 lg:border-l-2 border-[#1E9B8F] dark:border-[#69D3C9]">
                <a href={"#/article/" + articleID} class="text-[1.25rem] lg:text-[1.50rem] text-color-body w-full">
                    {articleTitle}
                </a>
            </div>
        </div>
    </div>
</div>

<style>
  
</style>
