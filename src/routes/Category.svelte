<script>
  import Header from "../components/Header.svelte";
  import CategoryTemplate from "./templates/CategoryTemplate.svelte";
  import Footer from "../components/Footer.svelte";
  import { apiLink } from "../stores";

  export let params = {};
  let categoryID = params.id;

  let content = [
    {
      gamename: "God of War",
      aboutText: "God of War is an action-adventure video game developed by Santa Monica Studio and published by Sony Interactive Entertainment. It was released on April 20, 2018 for PlayStation 4 and on January 14, 2022 for Microsoft Windows.",
      image: {
        src: "",
        alt: ""
      },
      section: [
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
    },
  ];

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
  <CategoryTemplate {...content[0]} />
  <Footer />
</div>
