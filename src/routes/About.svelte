<script>
  import Header from ".././components/Header.svelte";
  import MainAbout from "../components/about_page/MainAbout.svelte";
  import SimpleSection from ".././components/SimpleSection.svelte";
  import Footer from ".././components/Footer.svelte";

  let src = "../public/backgroundImageAbout.svg";
</script>

<div class="w-full min-h-screen bg-[#001219]">
  <Header className="sticky top-0" />
  <MainAbout />
  <Footer />
</div>
