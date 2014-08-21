community
=========

merge together [wellness](https://github.com/warmwaffles/wellness) compatible
checks to build a unified view of your conglomerated services

# Routes

- `/health/status`

    returns as wellness does, but does not handle `DEGRADED` status

- `/health/details`

    returns a wellness like `status`, `services`, `details` hash with combined `services` and `details` dictionaries by `name`

# Configuraiton

`community` accepts one and only one environment variable!

- `COMMUNITY_MEMBERS`: a `|` separated list of `,` separated (name, health url)
pairs
  * example: `core-api,https://core.example.com/health|user-api,https://user.example.com/health`
will produce approximately this output

```
$ curl conglomo.example.com/health/status
{"status":"HEALTHY"}
$ curl conglomo.example.com/health/details
{
  "status": "HEALTHY",
  "services": {
    "core-api": {
      "mysql": {
        "status": "HEALTHY",
        "details": {}
      }
    },
    "user-api": {
      "database": {
        "status": "HEALTHY",
        "details": {}
      },
      "sidekiq": {
        "status": "HEALTHY",
        "details": {
          "busy": 0,
          "default_latency": 104502.181265831,
          "enqueued": 290,
          "failed": 6045,
          "processed": 10982,
          "redis": {
            "connected_clients": "158",
            "uptime_in_days": "224",
            "used_memory_human": "4.19M",
            "used_memory_peak_human": "8.14M"
          },
          "retries": 3,
          "scheduled": 0
        }
      }
    }
  },
  "details": {
    "core-api": {
      "git": {
        "revision": "deadbeef"
      }
    },
    "user-api": {
      "git": {
        "revision": "deadbeef"
      }
    }
  }
}
```
