<script>
  import Header from "../../components/Header.svelte";
  import Footer from "../../components/Footer.svelte";
  import SimpleSection from "../../components/SimpleSection.svelte";

  export let gameName;
  export let image;
  export let aboutText;
  export let sections;
</script>

<!-- estilização temporária até adição de uma categoria para visualizar como ficou e melhorar o que for necessário-->
<div class="w-full h-full bg-green-500">
  <div class="bg-red-600 mx-auto md:h-3/4 w-full aspect-video">
    <img src={image.src} alt={image.alt} class="w-full h-full">
  </div>
  <div class="bg-purple-500 w-full h-96">
    <h1 class="md:text-2xl text-xl text-color-title">
        {gameName}
    </h1>
    <p class="md:text-lg text-base text-color-body text-justify break-words">
      {aboutText}
    </p>
  </div>
  <div class="">
    {#each sections as sectionData}
    <SimpleSection {...sectionData} />
    {/each}
  </div>
</div>
