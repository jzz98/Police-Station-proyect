const sidebar = {
    template: `
    <aside class="aside is-placed-left is-expanded">
  <div class="aside-tools">
    <div>
      Admin <b class="font-black">One</b>
    </div>
  </div>
  <div class="menu is-menu-main">
    <p class="menu-label">General</p>
    <ul class="menu-list">
      <li class="active">
        <a href="/admin">
          <span class="icon"><i class="mdi mdi-desktop-mac"></i></span>
          <span class="menu-item-label">Dashboard</span>
        </a>
      </li>
    </ul>
    <p class="menu-label">Examples</p>
    <ul class="menu-list">
      <li class="--set-active-tables-html">
        <a href="/admin/register-recluses">
          <span class="icon"><i class="mdi mdi-table"></i></span>
          <span class="menu-item-label">Register Recluses</span>
        </a>
      </li>
      <li class="--set-active-forms-html">
        <a href="/admin">
          <span class="icon"><i class="mdi mdi-square-edit-outline"></i></span>
          <span class="menu-item-label">Forms</span>
        </a>
      </li>
      <li class="--set-active-profile-html">
        <a href="profile.html">
          <span class="icon"><i class="mdi mdi-account-circle"></i></span>
          <span class="menu-item-label">Profile</span>
        </a>
      </li>
      <li>
        <a href="login.html">
          <span class="icon"><i class="mdi mdi-lock"></i></span>
          <span class="menu-item-label">Login</span>
        </a>
      </li>
      <li>
        <a class="dropdown">
          <span class="icon"><i class="mdi mdi-view-list"></i></span>
          <span class="menu-item-label">Submenus</span>
          <span class="icon"><i class="mdi mdi-plus"></i></span>
        </a>
        <ul>
          <li>
            <a href="#void">
              <span>Sub-item One</span>
            </a>
          </li>
          <li>
            <a href="#void">
              <span>Sub-item Two</span>
            </a>
          </li>
        </ul>
      </li>
    </ul>
    <p class="menu-label">About</p>
    <ul class="menu-list">
      <li>
        <a href="https://justboil.me" onclick="alert('Coming soon'); return false" target="_blank" class="has-icon">
          <span class="icon"><i class="mdi mdi-credit-card-outline"></i></span>
          <span class="menu-item-label">Premium Demo</span>
        </a>
      </li>
      <li>
        <a href="https://justboil.me/tailwind-admin-templates" class="has-icon">
          <span class="icon"><i class="mdi mdi-help-circle"></i></span>
          <span class="menu-item-label">About</span>
        </a>
      </li>
      <li>
        <a href="https://github.com/justboil/admin-one-tailwind" class="has-icon">
          <span class="icon"><i class="mdi mdi-github-circle"></i></span>
          <span class="menu-item-label">GitHub</span>
        </a>
      </li>
      <li>
        <a href="/logout" class="has-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path fill="currentColor" d="M4 20V4h8.02v1H5v14h7.02v1zm12.462-4.461l-.702-.72l2.319-2.319H9.192v-1h8.887l-2.32-2.32l.702-.718L20 12z"/></svg>          
          <span class="menu-item-label">Logout</span>
        </a>
      </li>
    </ul>
  </div>
</aside>
`
}

Vue.createApp(sidebar).mount('#sidebar')