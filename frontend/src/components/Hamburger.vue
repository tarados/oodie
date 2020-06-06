<template>
  <div class="menu-wrap">
    <input type="checkbox" class="toggler">
    <div class="hamburger">
      <div></div>
    </div>
    <div class="menu">
      <div>
        <div>
          <ul>
            <li><a href="#">Home</a></li>
            <li>
              <a href="#">Sale Products</a>
            </li>
            <li>
              <a href="#">Contact us</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

    export default {
        name: "Hamburger",
        components: {},
        data() {
            return {
                show: true
            }
        }
    }
</script>

<style>
  :root {
    --primary-color: rgba(13, 110, 139, 0.1);
    --overlay-color: rgba(24, 39, 51, 0.55);
    --menu-speed: 0.75s;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: "Roboto", sans-serif;
    line-height: 1.4;
  }

  .menu-wrap {
    position: fixed;
    top: 4.4vw;
    left: 0;
    z-index: 1;
  }

  .menu-wrap .toggler {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 2;
    cursor: pointer;
    width: 50px;
    height: 50px;
    opacity: 0;
  }

  .menu-wrap .hamburger {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 1;
    width: 60px;
    height: 60px;
    padding: 1rem;
    background-color: var(--primary-color);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .menu-wrap .hamburger > div {
    position: relative;
    width: 100%;
    height: 2px;
    background-color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.4s ease;
  }

  .menu-wrap .hamburger > div:before,
  .menu-wrap .hamburger > div::after {
    content: '';
    position: absolute;
    z-index: 1;
    top: -10px;
    width: 100%;
    height: 2px;
    background: inherit;
  }

  .menu-wrap .hamburger > div:after {
    top: 10px;
  }

  .menu-wrap .toggler:checked + .hamburger > div {
    transform: rotate(135deg);
  }

  .menu-wrap .toggler:checked + .hamburger > div:before,
  .menu-wrap .toggler:checked + .hamburger > div:after {
    top: 0;
    transform: rotate(90deg);
  }

  .menu-wrap .toggler:checked:hover + .hamburger > div {
    transform: rotate(225deg);
  }

  .menu-wrap .toggler:checked ~ .menu {
    visibility: visible;
  }

  .menu-wrap .toggler:checked ~ .menu > div {
    transform: scale(1);
    transition-duration: var(--menu-speed);
  }

  .menu-wrap .toggler:checked ~ .menu > div > div {
    opacity: 1;
    transition: opacity 0.4s ease;
  }

  .menu-wrap .menu {
    position: fixed;
    top: 82px;
    left: 0;
    width: 100%;
    height: 164px;
    visibility: hidden;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .menu-wrap .menu > div {
    background: var(--overlay-color);
    border-radius : 50%;
    width: 200vw;
    height: 200vw;
    display: flex;
    flex: none;
    align-items: center;
    justify-content: center;
    transform: scale(0);
    transition: all 0.4s ease;
  }

  .menu-wrap .menu > div > div {
    text-align: center;
    max-width: 90vw;
    max-height: 100vh;
    opacity: 0;
    transition: opacity 0.4s ease;
  }

  .menu-wrap .menu > div > div > ul > li {
    list-style: none;
    color: #fff;
    font-size: 1.11rem;
    border-bottom: 1px solid white;
    padding: 0.65rem;
  }

  .menu-wrap .menu > div > div > ul > li > a {
    color: inherit;
    text-decoration: none;
    transition: color 0.4s ease;
  }

</style>