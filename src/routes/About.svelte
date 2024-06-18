<script>
  import Header from ".././components/Header.svelte";
  import MainAbout from "../components/about_page/MainAbout.svelte";
  import AboutDevTemplate from "../components/about_page/AboutDevTemplate.svelte";
  import Footer from ".././components/Footer.svelte";

  let src = "../public/backgroundImageAbout.svg";

  let valores = [
    { name: "Fellipe Leonardo Peixoto Cunha", description: "Mó paz" },
    { name: "Matheus Jorge Santana", description: "" },
    { name: "Bárbara Fernandes Rampazi", description: "" },
    { name: "Henrique", description: "" },
    { name: "Lucas Tino Rosa", description: "" },
  ];
</script>

<div class="w-full min-h-screen bg-[#001219]">
  <Header className="sticky top-0" />
  <MainAbout />
  <div class="flex items-center justify-center m-5">
    <h1
      class="text-[#69D3C9] text-[36px] font-title-semibold block text-center"
    >
      Our Team
    </h1>
  </div>
  <div>
    {#each valores as valor}
      <AboutDevTemplate {...valor} />
    {/each}
  </div>
  <div class="flex items-center justify-center m-10">
    <h2 class="text-white text-[36px] font-title-bold block text-center">
      Success is not definitive, failure is not fatal: It is the courage to
      continue that counts.
    </h2>
  </div>
  <Footer />
</div>
