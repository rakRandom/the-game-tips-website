<script>
    import Router from 'svelte-spa-router';

    import Index from './routes/Index.svelte';
    import Help from './routes/Help.svelte';
    import NotFound from './routes/NotFound.svelte';
    import Admin from './routes/Admin.svelte';
    import About from './routes/About.svelte';
    import Category from './routes/Category.svelte';
    import Contact from './routes/Contact.svelte';
    import Article from './routes/Article.svelte';
    import CreateAccount from './routes/CreateAccount.svelte';
    import UserPage from './routes/UserPage.svelte';
    import Login from './routes/Login.svelte';

    let routes = {
        '/': Index,
        '/help': Help,
        '/about': About,
        '/contact': Contact,
        '/login': Login,
        '/create-account': CreateAccount,
        '/user/:id': UserPage,
        '/article/:id': Article,
        '/category/:id': Category,
        '/admin': Admin,
        '*': NotFound
    }
</script>

<main>
    <Router {routes} />
</main>
