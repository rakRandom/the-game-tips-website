<script>
    import { fetchImage } from "../../api/api_connection";

    export let game;
    export let title;
    export let image;
    export let info;
  </script>
  
  <div class="gap-32 md:max-w-[1024px] md:mx-auto md:py-10 py-5 border-b-2 border-[#69D3C9] mb-10 px-[16px]">
    <h1 class="md:text-4xl text-2xl text-color-title font-title-semibold mb-4 uppercase break-all hover:underline">
        <a href={"#/category/" + game.src}>{game.name}</a>
    </h1>
    <h3 class="md:text-4xl text-2xl font-title-regular mb-5">
        {title}
    </h3>
    <div class="">
        <img src={fetchImage(image.src)} alt="{image.alt}" class="mb-8 w-full h-full" />
    </div>
    <div class="items-center flex flex-row">
        <a href="/#/user/0i{info.author.id}">
            <img src={info.author.imgSrc} alt="" class="md:h-10 h-8 rounded-full" />
        </a>
        <p class="text-color-title ms-2 break-all md:text-lg text-base">
            By <a href="/#/user/0i{info.author.id}" class="hover:underline">{info.author.name}</a> • {info.date}
        </p>
    </div>
  </div>
  