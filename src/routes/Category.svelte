<script>
  import { fetchImage } from "../api/api_connection";

  import Header from "../components/Header.svelte";
  import Footer from "../components/Footer.svelte";
  import { apiLink } from "../stores";
  import SimpleSection from "../components/SimpleSection.svelte";
  import PopUpArticle from "../components/PopUpArticle.svelte";

  export let params = {};
  let categoryID = params.id;

  let content = {
    gameName: "",
    aboutText: "",
    image: {
      src: "",
      alt: ""
    },
    sections: [
      {
        title: "", 
        seeAllPage: "",
        contents: [
          { 
            gameName: "", 
            title: "", 
            authorPhotoSrc: "", 
            authorName: "", 
            postDate: "", 
            articlePage: ""
          },
          { 
            gameName: "", 
            title: "", 
            authorPhotoSrc: "", 
            authorName: "", 
            postDate: "", 
            articlePage: ""
          },
          { 
            gameName: "", 
            title: "", 
            authorPhotoSrc: "", 
            authorName: "", 
            postDate: "", 
            articlePage: ""
          },
          { 
            gameName: "", 
            title: "", 
            authorPhotoSrc: "", 
            authorName: "", 
            postDate: "", 
            articlePage: ""
          },
          { 
            gameName: "", 
            title: "", 
            authorPhotoSrc: "", 
            authorName: "", 
            postDate: "", 
            articlePage: ""
          },
        ]
      },
    ]
  };

  async function getContent() {
    let payload = await fetch({$apiLink} + "category/" + categoryID);
    let request = await payload.json();

    if (!request)
        return;

    content = request;
  }

  getContent();
</script>

<div class="bg-color-0">
  <Header className="sticky top-0" />
  <div class="w-full max-w-[1280px] lg:min-w-[1024px] h-fit lg:min-h-[500px] mx-auto bg-color-mid mb-20">
    <div class="mx-auto md:h-3/4 w-full aspect-video">
      <img src={fetchImage(content.image.src)} alt={content.image.alt} class="w-full h-full">
    </div>
    <div class="w-full h-full md:space-y-5 space-y-3 p-5">
      <h1 class="md:text-6xl text-4xl text-color-title text-center uppercase">
          {content.gameName}
      </h1>
      <p class="md:text-xl text-base text-color-body text-justify break-words">
          {content.aboutText}
      </p>
    </div>
    <div class="dark:bg-[#001A24] bg-[#EEE] py-4">
      {#each content.sections as sectionData}
      <SimpleSection elementType={PopUpArticle} {...sectionData} />
      {/each}
    </div>
  </div>
  <Footer />
</div>
