<script>
    import { fetchImage } from "../api/api_connection";

    export let className = "";
    export let imgSrc;
    export let gameName;
    export let title;
    export let authorPhotoSrc;
    export let authorName;
    export let postDate;
    export let articlePage;
</script>

<div class="h-[280px] min-w-[220px] max-w-[220px] {className}">
    <div class="relative w-full h-[75%]">
        <img src={fetchImage(imgSrc)} alt="" class="w-full h-full object-cover rounded-lg">
        <a href={"#/article/" + articlePage} class="absolute w-full h-[53%] -bottom-16">
            <div class="flex w-full h-full justify-center pt-1 hover:-translate-y-1 transition-transform">
                <div class="flex flex-col text-center w-[90%] h-full bg-color-mid rounded-md overflow-hidden cursor-pointer">
                    <div class="flex-1 py-1 px-1">
                        <h3 class="font-title-medium text-color-title uppercase pb-1"> {gameName} </h3>
                        <p class="text-sm line-clamp-2 text-color-body"> {title} </p>
                    </div>
                    <a href="/" class="flex items-center gap-2 text-[14px] font-light p-1 bg-[#051D26]">
                        <img src={fetchImage(authorPhotoSrc)} alt="" class="inline-block h-6 aspect-square border-[1px] border-[#69D3C9BE] rounded-full">
                        <span class="text-[#69D3C9BE] w-full text-center">By {authorName} - {postDate}</span>
                    </a>
                </div>
            </div>
        </a>
    </div>
</div>

<style>
  
</style>
