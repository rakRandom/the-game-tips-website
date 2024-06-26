<script>
    import Router from 'svelte-spa-router';

    import Index         from './routes/Index.svelte';
    import Help          from './routes/Help.svelte';
    import About         from './routes/About.svelte';
    import Contact       from './routes/Contact.svelte';
    import Login         from './routes/Login.svelte';
    import CreateAccount from './routes/CreateAccount.svelte';
    import UserPage      from './routes/UserPage.svelte';
    import Article       from './routes/Article.svelte';
    import Category      from './routes/Category.svelte';
    import Admin         from './routes/Admin.svelte';
    import NotFound      from './routes/NotFound.svelte';

    let routes = {
        '/': Index,

        '/help'   : Help,
        '/about'  : About,
        '/contact': Contact,

        '/login'         : Login,
        '/create-account': CreateAccount,

        '/user/:id'    : UserPage, // Params: isUser, userID (separator "i")
        '/article/:id' : Article,
        '/category/:id': Category,

        '/admin': Admin,
        '*'     : NotFound
    }

    const loaded = () => {
        window.scrollTo(0,0);
    }
</script>

<main>
    <Router {routes} on:routeLoaded={loaded} />
</main>
