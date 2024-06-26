<script>
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

<div>
  <Header className="sticky top-0" />
  <div class="w-full h-full bg-green-500">
    <div class="bg-red-600 mx-auto md:h-3/4 w-full aspect-video">
      <img src={content.image.src} alt={content.image.alt} class="w-full h-full">
    </div>
    <div class="bg-purple-500 w-full h-96">
      <h1 class="md:text-2xl text-xl text-color-title">
          {content.gameName}
      </h1>
      <p class="md:text-lg text-base text-color-body text-justify break-words">
        {content.aboutText}
      </p>
    </div>
    <div class="">
      {#each content.sections as sectionData}
      <SimpleSection elementType={PopUpArticle} {...sectionData} />
      {/each}
    </div>
  </div>
  <Footer />
</div>
