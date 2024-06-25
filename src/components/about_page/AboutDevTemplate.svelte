<script>
    import { fetchImage } from "../../api/api_connection";

    export let name;
    export let image; 
    export let linkedin; 
    export let github; 
    export let whatsapp; 
    export let email; 
    export let description; 
</script>

<div class="pb-10">
    <div class="flex flex-wrap rounded-t-full rounded-b-[150rem] md:rounded-l-full md:rounded-r-[150rem] md:h-56 md:w-full h-auto w-72 mx-auto bg-none overflow-hidden">
        <div class="rounded-t-3xl flex md:flex-row flex-col dark:bg-[#001219] bg-[#DFDFDF] md:text-left text-center md:pt-1 md:ps-40 md:h-12 md:w-full pt-72 text-lg h-[375px] w-72 md:ms-24 z-[5]">
            <p class="w-full h-fit text-lg md:pt-2 pt-3 font-semibold text-[#69D3C9] line-clamp-1" title={name}>{name}</p>
            <!-- Social Media Icons -->
            <div class="w-full flex flex-row space-x-3 md:justify-end justify-center md:pe-8 pt-1">
                <a href="{linkedin}" class="h-8 w-8">
                    <img src="static/media/img/icons8-linkedin.svg" alt="Logo linkedin">
                </a>
                <a href="{github}" class="h-8 w-8">
                    <img src="static/media/img/icons8-github.svg" alt="Logo github">
                </a>
                <a href="https://web.whatsapp.com/send?phone={whatsapp}" class="h-8 w-8">
                    <img src="static/media/img/icons8-whatsapp.svg" alt="Logo whatsapp">
                </a>
                <a href="mailto:{email}">
                    <img src="static/media/img/mail_24dp_FILL0_wght400_GRAD0_opsz24.svg" alt="Logo email" class="h-8 w-8">
                </a>
            </div>
        </div>
        <img class="absolute h-72 w-72 md:h-56 md:w-56 rounded-full z-[5] object-cover" src={fetchImage(image)} alt="">
        <p class="dark:bg-[#051D26] bg-[#EEEEEE] md:ps-64 md:pt-3 md:text-lg md:pe-12 md:h-full md:w-full px-4 pt-3 pb-3 text-color-body">{description}</p>
    </div>
</div>

<style>

</style>