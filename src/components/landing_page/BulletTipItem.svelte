<script>
    import { fetchImage } from "../../api/api_connection";

    export let className = "";

    export let name;
    export let phrase;
    export let articleID = "#";
    export let icon;
    export let image;

    let visibility = "hidden";
    let show = () => {visibility = "";};
    let hide = () => {visibility = "hidden";};
</script>

<div class="flex flex-col items-center 
            min-h-[90px] w-[100px] mt-1 
            hover:cursor-pointer hover:-translate-y-1 
            transition-transform {className}"
    >
    <button type="button" 
            on:click={show} 
            class="flex items-center justify-center w-[90px] h-[90px] rounded-full bg-gradient-to-tr from-[#2EC4B6] to-[#FF2202] overflow-hidden drop-shadow-md"
            >
            <div class="w-[82px] h-[82px] rounded-full bg-white">
                <img src="{fetchImage(icon)}" alt="Bullet icon" class="rounded-full">
            </div>
    </button>

    <h1 class="text-center text-color-title h-fit break-words">
        {name}
    </h1>
</div>

<div class="{visibility} fixed z-50 top-0 left-0 w-svw h-svh bg-[#00000020] backdrop-blur-sm">
    <div class="flex flex-col sm:gap-4 items-center justify-center h-full w-full">
        <div class="flex flex-col relative w-full h-full sm:w-[380px] sm:h-[560px] bg-[#051D26] rounded-xl overflow-hidden">
            <button type="button" on:click={hide} 
                class="absolute top-2 right-2 w-[30px] h-[30px] pb-[1px] bg-[#000000A0] rounded-full opacity-75 hover:opacity-100">
                X
            </button>
            <img src={fetchImage(image)} alt="" class="w-full h-full sm:h-[560px] object-cover">
            <div class="flex items-end h-[100px] w-full">
                <div class="bg-[#001219] min-h-[100px] w-full px-4 py-2">
                    {phrase}
                </div>
            </div>
            <a href={"#/article/" + articleID} class="group text-[#69D3C9] text-center py-1">
                Want to see more? Check out the complete tip ;)
                <hr class="w-0 mx-auto border-[#69D3C9] 
                           group-hover:w-[75%]
                           transition-all duration-500">
            </a>
        </div>
        <div>
            
        </div>
    </div>
</div>

<style>
  
</style>
