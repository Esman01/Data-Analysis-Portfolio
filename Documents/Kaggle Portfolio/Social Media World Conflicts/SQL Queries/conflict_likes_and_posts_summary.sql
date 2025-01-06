SELECT conflict, 
       COUNT(*) AS TotalPosts, 
       SUM(likes) AS TotalLikes, 
FROM EngagementData
GROUP BY conflict
ORDER BY TotalViews DESC;