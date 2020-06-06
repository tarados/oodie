<template>
  <div>
    <Navbar/>
    <Hamburger/>
    <header class="showcase">
      <div class="container showcase-inner">
        <h1>Winter Sale Now On!</h1>
        <p>One size fits all hooded blanket perfect for those chilly mornings and cold afternoons!</p>
        <a href="#" class="btn">BUY NOW</a>
      </div>
    </header>
  </div>
</template>

<script>
    import Navbar from "../components/Navbar";
    import Hamburger from "../components/Hamburger"

    export default {
        name: 'Home',
        components: {
            Navbar,
            Hamburger
        }
    }
</script>

<style>
  .shopContent {
    position: absolute;
    width: 100%;
    height: 650px;
  }

  .container {
    max-width: 960px;
    margin: auto;
    overflow: hidden;
    padding: 0.3rem;
  }

  .showcase {
    background-color: var(--primary-color);
    color: white;
    height: 100vh;
    position: relative;
  }

  .showcase:before {
    content: '';
    background: url("../assets/tile.jpg") no-repeat center center/cover;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 650px;
    z-index: -1;
  }

  .showcase .showcase-inner {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    height: 100%;
  }

  .showcase h1 {
    font-size: 2.5rem;
  }

  .showcase p {
    font-size: 1.2rem;
  }

  .btn {
    display: inline-block;
    border: none;
    border-radius: 3px;
    background-color: white;
    color: black;
    padding: 0.75rem 1.5rem;
    margin-top: 1rem;
    text-decoration: none;
    transition: opacity 1s ease-in;
  }

  .btn:hover {
    opacity: 0.7;
  }

  @media screen and (max-width: 750px) {

  }

</style>
