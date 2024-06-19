<script>
  import Header from ".././components/Header.svelte";
  import MainAbout from "../components/about_page/MainAbout.svelte";
  import AboutDevTemplate from "../components/about_page/AboutDevTemplate.svelte";
  import Footer from ".././components/Footer.svelte";

  let valores = [
    { 
      name: "Fellipe Leonardo Peixoto Cunha", 
      image: "", 
      linkedin: "", 
      github: "", 
      whatsapp: "",  
      email: "", 
      description: "" 
    },
    { 
      name: "Matheus Jorge Santana", 
      image: "", 
      linkedin: "", 
      github: "", 
      whatsapp: "",  
      email: "", 
      description: "" 
    },
    { 
      name: "Bárbara Fernandes Rampazi", 
      image: "", 
      linkedin: "", 
      github: "", 
      whatsapp: "",  
      email: "", 
      description: "" 
    },
    { 
      name: "Henrique da Silva Macedo",
      image: "", 
      linkedin: "", 
      github: "", 
      whatsapp: "",  
      email: "", 
      description: "" 
    },
    { 
      name: "Lucas Tino Rosa", 
      description: "I am a student on a Systems Development course. Throughout my studies, I have had many experiences with the process of creating a website, and The Game Tips is the most recent of them. When I'm not programming or studying, I like to play games (mostly looking for secrets), write stories, and hang out with my friends, some of whom you've already met by reading this page.", 
      image: "../src/assets/img/AboutDevs/LTR.jpeg",
      linkedin: "/", 
      github: "https://github.com/Lucas-Tino", 
      whatsapp: "11914836435",  
      email: "lucastino2007@gmail.com"
    }
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
    <h2 class="text-white text-[36px] font-title-bold block text-center my-36 px-[100px]">
      Success is not definitive, failure is not fatal: It is the courage to
      continue that counts.
    </h2>
  </div>
  <Footer />
</div>
