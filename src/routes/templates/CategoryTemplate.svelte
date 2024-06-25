<script>
  import Header from "../../components/Header.svelte";
  import Footer from "../../components/Footer.svelte";
  import SimpleSection from "../../components/SimpleSection.svelte";

  export let gameName;
  export let image;
  export let aboutText;
  export let sections;
</script>

<div class="">
  <Header />
  <div class="">
    <img src={image.src} alt={image.alt}>
    <h1 class="">
      {gameName}
    </h1>
  </div>
  <div class="">
    <p class="">
      {aboutText}
    </p>
  </div>
  <div class="">
    {#each sections as sectionData}
    <SimpleSection {...sectionData} />
    {/each}
  </div>
  <Footer />
</div>
