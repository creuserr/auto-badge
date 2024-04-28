> [!NOTE]
> I am no longer maintaining this repository; nevertheless, you can still use it.

# auto-badge
Statically generated Markdown badges for your GitHub repositories' README

<br><div align="center">

![Starazers](https://auto-badge.vercel.app/api/star/creuserr/auto-badge)
![Watchers](https://auto-badge.vercel.app/api/watch/creuserr/auto-badge)
![Subscribers](https://auto-badge.vercel.app/api/sub/creuserr/auto-badge)
![Forks](https://auto-badge.vercel.app/api/fork/creuserr/auto-badge)
![Open Issues](https://auto-badge.vercel.app/api/issue/creuserr/auto-badge)

</div>

## Usage

```html
https://auto-badge.vercel.app/api/<METHOD>/<USER>/<REPO>
```

| Method | For | Example URL |
|:-----:|:-----:|:-----:|
| `/star` | Stargazers | [/star/creuserr/auto-badge](https://auto-badge.vercel.app/api/star/creuserr/auto-badge) |
| `/watch` | Watchers | [/watch/creuserr/auto-badge](https://auto-badge.vercel.app/api/watch/creuserr/auto-badge) |
| `/sub` | Subscribers | [/sub/creuserr/auto-badge](https://auto-badge.vercel.app/api/sub/creuserr/auto-badge) |
| `/fork` | Forks | [/fork/creuserr/auto-badge](https://auto-badge.vercel.app/api/fork/creuserr/auto-badge) |
| `/issue` | Open Issues | [/issue/creuserr/auto-badge](https://auto-badge.vercel.app/api/issue/creuserr/auto-badge) |

## Additional headers
Auto-badge apply additional headers when redirecting to **img.shields.io**.

```http
GET https://auto-badge.vercel.app/api/star/creuserr/auto-badge
```

| Header | For | Example |
|:------:|:---:|:-------:|
| `X-Autobadge-Version` | Version of auto-badge | 3 |
| `X-Autobadge-Method` | Requested method | star |
| `X-Autobadge-User` | Provided username | creuserr |
| `X-Autobadge-Repo` | Provided repository | auto-badge |
| `X-Autobadge-Value` | Value of the request | 1 (detected 1 stargazer) |

## Deploy your own
Auto-badge's main serverless function strictly don't accept heavy queue due to GitHub free API's limitation.

You are free to deploy your own, personalize by your style, and use your own API account. Simply fork this repository, adjust it all you want, and deploy it to Vercel.

<div align="center">

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fcreuserr%2Fauto-badge%2Ftree%2Fmain)

</div><br>

### Third-party libraries

*This service heavily utilizes and accredits __shields.io.__*
