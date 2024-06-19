<script>
  import Header from ".././components/Header.svelte";
  import MainAbout from "../components/about_page/MainAbout.svelte";
  import AboutDevTemplate from "../components/about_page/AboutDevTemplate.svelte";
  import Footer from ".././components/Footer.svelte";

  let valores = [
    { 
      name: "Fellipe Leonardo Peixoto Cunha", 
      image: "public/images_autores/fellipe.png", 
      linkedin: "https://www.linkedin.com/in/fellipe-leonardo", 
      github: "https://github.com/rakRandom", 
      whatsapp: "11993792647",  
      email: "fellipeleo100@gmail.com", 
      description: "I'm a student of Systems Development course integrated with High School, passionate about technology, programming and all the things relationed to Computer Science. Future software engineer looking for innovative solutions." 
    },
    { 
      name: "Matheus Jorge Santana", 
      image: "public/images_autores/matheus.jpeg", 
      linkedin: "https://www.linkedin.com/in/henrique-da-silva-macedo-0255942b7/", 
      github: "https://github.com/HickSouldrow", 
      whatsapp: "11984912520",  
      email: "henriquedasilvamacedo6@gmail.com", 
      description: "Hello, I'm \"17\" years old and my dream is to become a pokem... an efficient worker! I'm also a good programmer, great student, and the best Minecraft player"
    },
    { 
      name: "Bárbara Fernandes Rampazi", 
      image: "/", 
      linkedin: "/", 
      github: "https://github.com/caramelPopp", 
      whatsapp: "11977577701",  
      email: "rampazibarbara1203@gmail.com", 
      description: "Hi! I'm a 16-year-old student who enjoys visual arts and who needs tips recurrently to pass the levels of the games"
    },
    { 
      name: "Henrique da Silva Macedo",
      image: "", 
      linkedin: "https://www.linkedin.com/in/matheus-jorge-santana-1436462b9/", 
      github: "https://github.com/mathsant-js", 
      whatsapp: "11988553256",  
      email: "mjorgesantana2007@gmail.com", 
      description: "I'm a 16-year-old student, I like learning new and current things, always keeping up to date with new technologies, I like programming and playing games."
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
