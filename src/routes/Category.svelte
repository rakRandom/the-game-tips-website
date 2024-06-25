<script>
  import Header from "../components/Header.svelte";
  import CategoryTemplate from "./templates/CategoryTemplate.svelte";
  import Footer from "../components/Footer.svelte";
  import { apiLink } from "../stores";

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
  <CategoryTemplate {...content} />
  <Footer />
</div>
