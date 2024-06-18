<script>
  let src = "../public/backgroundImageAbout.svg";
  let logoImage = "../public/logoImage.svg";
</script>

<div class="flex items-center justify-center">
  <img {src} alt="Backgound svg" class="w-full h-auto" />
  <div class="absolute z-0">
    <div
      class="flex items-center justify-between bg-black bg-center opacity-75 w-[990px] h-[390px] p-5"
    >
    <div>

      <h1 class="text-[#69D3C9] text-[36px] font-title-semibold block">About Us</h1>
      <p class="text-white w-[40rem] text-justify">
        The Game Tips is a website that focuses on sharing tips with gamers,
        helping them get through hard levels and challenges, or be better at
        online games. The idea for this project came from our team’s own
        experiences with gaming, as well as our passion for games. We started
        out in 2024, and have been providing information for gamers since then.
        More hypothetical text about the developers and the idea itself,
        describing our motivations, dreams, past, personal data, real-life
        addresses, IP addresses, literally just typing anything to fill space
        and give a better idea of how this could look if it had more text, so
        just ignore everything past the first two paragraphs alright?
      </p>
    </div>

      <div class="absolute inset-y-0 right-0 flex items-center p-4">
        <img src={logoImage} alt="Logo" class="w-[250px] h-[275px]" />
      </div>
    </div>
  </div>
</div>
