<script>
  import Header from "../../components/Header.svelte";
  import Footer from "../../components/Footer.svelte";
  import PopUpArticle from "../../components/PopUpArticle.svelte";
  
  // A imagem é só pra testar
  let src = "../src/assets/img/Multiversus/multiversusImage.png";

  export let gamename;
  export let aboutText;

  let values = [
    {
      className: "",
      gameName: "",
      title: "",
      authorPhotoSrc: "",
      authorName: "",
      postDate: "",
      articlePage: "",
    },
  ];
</script>

<div
  class="w-full min-h-screen bg-[#F6F6F6] dark:bg-[#000B10] text-[#121212] dark:text-white"
>
  <main>
    <div class="flex flex-col flex-1 items-center justify-center">
      <img {src} alt="Backgound svg" class="w-full h-auto" />
      <div class="absolute z-0">
        <div
          class="flex items-center justify-center bg-black bg-center bg-opacity-90 w-[1440px] h-[670px] p-5"
        >
          <div class="">
            <h1
              class=" text-white dark:text-white font-title-bold text-8xl"
            >
              {gamename}
            </h1>
          </div>
        </div>
      </div>
    </div>
    <div class="flex flex-col flex-1 mt-16 items-center justify-center">
      <div>
        <h2
          class="text-5xl text-[#1E9B8F] dark:text-[#69D3C9] font-title-semibold"
        >
          ABOUT THIS GAME
        </h2>
      </div>
      <div class="text-2xl mt-12 m-5 mx-16">
        <p class="text-justify">{aboutText}</p>
      </div>
      <div class="flex flex-row flex-1 mx-20 my-5">
        {#each values as value}
          <PopUpArticle {...value} />
        {/each}
      </div>
    </div>
  </main>
</div>
